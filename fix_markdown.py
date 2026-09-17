#!/usr/bin/env python3.11
"""
Исправление однозначных опечаток и расстановка «ё» в Markdown-файлах.

Использование:
    python fix_markdown.py файл1.md файл2.md ...
    python fix_markdown.py --dry-run файл.md      # только отчёт, без записи
    python fix_markdown.py --no-yo файл.md        # только опечатки, без ёфикации
    python fix_markdown.py --no-spell файл.md     # только ёфикация
"""

import re
import sys
import argparse
from pathlib import Path

from spellchecker import SpellChecker

# ------------------------------------------------------------------
# Подключение yoficator (лежит в папке проекта)
# ------------------------------------------------------------------
def _load_yoficator():
    try:
        from yoficator import yoficate  # функция
        return yoficate
    except ImportError:
        pass
    try:
        from yoficator import Yoficator  # класс
        inst = Yoficator()
        return inst.yoficate
    except Exception as e:
        print(f"Ошибка: не удалось загрузить yoficator: {e}")
        print("Убедитесь, что yoficator.py и yoficator.dic лежат в папке проекта.")
        sys.exit(1)

yoficate = _load_yoficator()

# ------------------------------------------------------------------
# Настройки
# ------------------------------------------------------------------
MIN_WORD_LEN = 4          # не трогаем слова короче 4 букв
MAX_EDIT_DISTANCE = 1     # только опечатки в одном символе
CYR_WORD_RE = re.compile(r'[А-Яа-яЁё]{2,}')

# Маркеры для маскировки (Unicode Private Use Area — не встречаются в тексте)
MASK_OPEN = '\uE000'
MASK_CLOSE = '\uE001'


# ------------------------------------------------------------------
# Расстояние Левенштейна (без внешних зависимостей)
# ------------------------------------------------------------------
def levenshtein(a: str, b: str, max_d: int = 2) -> int:
    if a == b:
        return 0
    if abs(len(a) - len(b)) > max_d:
        return max_d + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            curr.append(min(
                prev[j] + 1,
                curr[j - 1] + 1,
                prev[j - 1] + (ca != cb),
            ))
        prev = curr
    return prev[-1]


# ------------------------------------------------------------------
# Маскировка фрагментов, которые нельзя трогать
# ------------------------------------------------------------------
def mask_special(text: str):
    """Скрывает inline-код, ссылки, HTML-теги и Liquid-вставки."""
    restore = {}
    counter = [0]

    def repl(m):
        key = f"{MASK_OPEN}{counter[0]:05d}{MASK_CLOSE}"
        counter[0] += 1
        restore[key] = m.group(0)
        return key

    text = re.sub(r'`[^`]*`', repl, text)                  # `code`
    text = re.sub(r'!?\[[^\]]*\]\([^)]*\)', repl, text)    # [text](url)
    text = re.sub(r'<[^>]+>', repl, text)                  # <tag>
    text = re.sub(r'\{[^{}]*\}', repl, text)               # {: .class }
    return text, restore


def unmask(text: str, restore: dict) -> str:
    for key, val in restore.items():
        text = text.replace(key, val)
    return text


# ------------------------------------------------------------------
# Исправление опечаток
# ------------------------------------------------------------------
def fix_typos(text: str, spell: SpellChecker, stats: dict) -> str:
    def repl(m):
        word = m.group(0)
        if len(word) < MIN_WORD_LEN:
            return word
        # pyspellchecker для русского хранит слова без «ё»
        lower = word.lower().replace('ё', 'е')
        if lower in spell:
            return word
        candidates = spell.candidates(lower)
        if not candidates:
            return word
        good = []
        for cand in candidates:
            cand_norm = cand.replace('ё', 'е')
            if cand_norm not in spell:
                continue
            if levenshtein(lower, cand_norm, MAX_EDIT_DISTANCE) > MAX_EDIT_DISTANCE:
                continue
            good.append(cand_norm)
        if len(good) == 1 and good[0] != lower:
            corrected = good[0]
            if word.isupper():
                corrected = corrected.upper()
            elif word[0].isupper():
                corrected = corrected.capitalize()
            stats['typos'].append((word, corrected))
            return corrected
        return word

    return CYR_WORD_RE.sub(repl, text)


# ------------------------------------------------------------------
# Обработка одной текстовой строки
# ------------------------------------------------------------------
def process_text_line(line: str, spell, stats, do_spell=True, do_yo=True) -> str:
    masked, restore = mask_special(line)
    if do_spell:
        masked = fix_typos(masked, spell, stats)
    if do_yo:
        try:
            masked = yoficate(masked)
        except Exception as e:
            stats['yof_errors'].append(str(e))
    return unmask(masked, restore)


# ------------------------------------------------------------------
# Обработка файла
# ------------------------------------------------------------------
def process_file(path: Path, spell, dry_run=False, do_spell=True, do_yo=True):
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    stats = {'typos': [], 'yof_errors': []}

    in_yaml = False
    in_code = False
    code_fence = None
    new_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # YAML frontmatter (только в самом начале)
        if i == 0 and stripped == '---':
            in_yaml = True
            new_lines.append(line)
            continue
        if in_yaml:
            if stripped == '---':
                in_yaml = False
            new_lines.append(line)
            continue

        # Блоки кода ``` или ~~~
        m = re.match(r'^\s*(```|~~~)', line)
        if m:
            if not in_code:
                in_code = True
                code_fence = m.group(1)
            elif code_fence and stripped.startswith(code_fence):
                in_code = False
                code_fence = None
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
            continue

        # Горизонтальные линии
        if re.fullmatch(r'\s*([-*_]\s*){3,}', line):
            new_lines.append(line)
            continue

        # Таблицы (часто с именами/числами)
        if '|' in line:
            new_lines.append(line)
            continue

        new_lines.append(process_text_line(line, spell, stats, do_spell, do_yo))

    new_text = '\n'.join(new_lines)
    changed = new_text != text

    if changed and not dry_run:
        path.write_text(new_text, encoding='utf-8')

    # -------- Отчёт --------
    print(f"\n=== {path} ===")
    if not changed:
        print("Изменений нет.")
    elif dry_run:
        print("[DRY-RUN] Изменения не записаны.")
    else:
        print("Файл обновлён.")

    if stats['typos']:
        print(f"Исправлено опечаток: {len(stats['typos'])}")
        seen = set()
        for old, new in stats['typos']:
            pair = (old, new)
            if pair in seen:
                continue
            seen.add(pair)
            print(f"  {old}  →  {new}")

    if stats['yof_errors']:
        print(f"Ошибки ёфикации ({len(stats['yof_errors'])}):")
        for e in set(stats['yof_errors']):
            print(f"  {e}")


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='+', help='Markdown-файлы')
    parser.add_argument('--dry-run', action='store_true',
                        help='Не записывать изменения')
    parser.add_argument('--no-yo', action='store_true',
                        help='Отключить ёфикацию')
    parser.add_argument('--no-spell', action='store_true',
                        help='Отключить исправление опечаток')
    args = parser.parse_args()

    print("Загружаю словарь русского языка...")
    spell = SpellChecker(language='ru')
    print("Готово.")

    for f in args.files:
        p = Path(f)
        if not p.is_file():
            print(f"[!] Пропущен (не файл): {p}")
            continue
        try:
            process_file(p, spell,
                         dry_run=args.dry_run,
                         do_spell=not args.no_spell,
                         do_yo=not args.no_yo)
        except Exception as e:
            print(f"[!] Ошибка при обработке {p}: {e}")


if __name__ == '__main__':
    main()