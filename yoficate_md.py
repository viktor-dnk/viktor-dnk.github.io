#!/usr/bin/env python3
"""
Ёфикация Markdown-файлов.

Заменяет «е» на «ё» только в словах из словаря yo_sure.txt
(однозначные случаи). Омографы и незнакомые слова не трогает.

Использование:
    python yoficate_md.py файл1.md файл2.md ...
    python yoficate_md.py --dry-run файл.md
    python yoficate_md.py --report файл.md
    python yoficate_md.py --dir _toponymy/2026
"""

import re
import sys
import argparse
from pathlib import Path

# ------------------------------------------------------------------
# Пути и настройки
# ------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
YO_DICT_PATH = SCRIPT_DIR / 'yo_sure.txt'

# Маркеры маскировки — Unicode Private Use Area, не встречаются в тексте
MASK_OPEN = '\uE000'
MASK_CLOSE = '\uE001'

CYR_WORD_RE = re.compile(r'[А-Яа-яЁё]+')


# ------------------------------------------------------------------
# Загрузка словаря
# ------------------------------------------------------------------
def load_yo_dict(path: Path):
    """
    Возвращает два множества:
      sure   — слова, где «ё» однозначна
      unsure — омографы, которые нельзя трогать
    Поддерживает два формата:
      'все / всё'  (yoditor)
      'всё'        (ruyo)
    """
    if not path.is_file():
        print(f"[!] Не найден словарь: {path}")
        print("    Скачайте yo_sure.txt или yo.txt и положите рядом со скриптом.")
        sys.exit(1)

    sure = set()
    unsure = set()
    total = 0

    with path.open(encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            total += 1
            if '/' in line:
                left, right = line.split('/', 1)
                left = left.strip().lower()
                right = right.strip().lower()
                if left:
                    unsure.add(left)
                if right:
                    sure.add(right)
            else:
                sure.add(line.lower())

    # Слова, которые встречаются и как sure, и как unsure — убираем из sure
    sure -= unsure
    print(f"Словарь загружен: {len(sure)} слов с «ё», {len(unsure)} омографов (всего {total} строк)")
    return sure, unsure


# ------------------------------------------------------------------
# Маскировка фрагментов, которые нельзя трогать
# ------------------------------------------------------------------
def mask_special(text: str):
    """Скрывает код, ссылки, HTML-теги и Liquid-вставки."""
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
# Ёфикация
# ------------------------------------------------------------------
def yoficate_text(text: str, sure: set, unsure: set, changes: list) -> str:
    """Заменяет «е» на «ё» в словах из sure, сохраняя регистр."""
    def repl(m):
        word = m.group(0)
        lower = word.lower()

        # Омографы — не трогаем
        if lower in unsure:
            return word

        # Слово не в словаре — не трогаем
        if lower not in sure:
            return word

        # Уже есть «ё» — не трогаем
        if 'ё' in lower:
            return word

        # Определяем, какая «е» должна стать «ё».
        # В словаре sure слово записано с «ё» — найдём позицию.
        # Для простоты заменяем первую «е»/«Е» (подавляющее большинство случаев).
        if word[0].isupper():
            new_word = word.replace('Е', 'Ё', 1) if 'Е' in word else word.replace('е', 'ё', 1)
        else:
            new_word = word.replace('е', 'ё', 1)

        if new_word != word:
            changes.append((word, new_word))
        return new_word

    return CYR_WORD_RE.sub(repl, text)


# ------------------------------------------------------------------
# Обработка одной строки
# ------------------------------------------------------------------
def process_line(line: str, sure: set, unsure: set, changes: list) -> str:
    masked, restore = mask_special(line)
    masked = yoficate_text(masked, sure, unsure, changes)
    return unmask(masked, restore)


# ------------------------------------------------------------------
# Обработка файла
# ------------------------------------------------------------------
def process_file(path: Path, sure: set, unsure: set,
                 dry_run=False, report_only=False, verbose=False):
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    changes = []

    in_yaml = False
    in_code = False
    code_fence = None
    new_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # YAML frontmatter
        if i == 0 and stripped == '---':
            in_yaml = True
            new_lines.append(line)
            continue
        if in_yaml:
            if stripped == '---':
                in_yaml = False
            new_lines.append(line)
            continue

        # Блоки кода
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

        # Таблицы
        if '|' in line:
            new_lines.append(line)
            continue

        new_lines.append(process_line(line, sure, unsure, changes))

    new_text = '\n'.join(new_lines)
    changed = new_text != text

    # -------- Вывод --------
    print(f"\n=== {path} ===")
    if not changes:
        print("Замен нет.")
        return

    print(f"Замен: {len(changes)}")
    if verbose:
        for old, new in changes:
            print(f"  {old}  →  {new}")
    else:
        # Уникальные пары
        seen = set()
        shown = 0
        for old, new in changes:
            if (old, new) in seen:
                continue
            seen.add((old, new))
            print(f"  {old}  →  {new}")
            shown += 1
            if shown >= 30:
                print(f"  ... и ещё {len(set(changes)) - shown} уникальных замен")
                break

    if report_only:
        return
    if dry_run:
        print("[dry-run] Файл не записан.")
        return
    if changed:
        path.write_text(new_text, encoding='utf-8')
        print("Файл обновлён.")


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------
def collect_files(args) -> list:
    files = []
    for f in args.files:
        p = Path(f)
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files.extend(sorted(p.rglob('*.md')))
        else:
            print(f"[!] Не найден: {p}")
    if args.dir:
        d = Path(args.dir)
        if d.is_dir():
            files.extend(sorted(d.rglob('*.md')))
        else:
            print(f"[!] Не найдена папка: {d}")
    # Убираем дубликаты, сохраняя порядок
    seen = set()
    unique = []
    for f in files:
        rp = f.resolve()
        if rp not in seen:
            seen.add(rp)
            unique.append(f)
    return unique


def main():
    parser = argparse.ArgumentParser(
        description='Ёфикация Markdown-файлов (только однозначные случаи).',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('files', nargs='*', help='Markdown-файлы или папки')
    parser.add_argument('--dir', help='Обработать все *.md в папке рекурсивно')
    parser.add_argument('--dry-run', action='store_true',
                        help='Показать замены, но не записывать файлы')
    parser.add_argument('--report', action='store_true',
                        help='Только отчёт, файлы не менять')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Показывать все замены (включая повторы)')
    parser.add_argument('--dict', default=str(YO_DICT_PATH),
                        help=f'Путь к словарю (по умолчанию {YO_DICT_PATH})')
    args = parser.parse_args()

    if not args.files and not args.dir:
        parser.print_help()
        sys.exit(1)

    sure, unsure = load_yo_dict(Path(args.dict))
    files = collect_files(args)

    if not files:
        print("Не найдено ни одного файла для обработки.")
        sys.exit(1)

    print(f"Файлов к обработке: {len(files)}")

    total_changes = 0
    for f in files:
        before = len(files)
        text_before_len = f.stat().st_size
        process_file(f, sure, unsure,
                     dry_run=args.dry_run,
                     report_only=args.report,
                     verbose=args.verbose)

    print(f"\nГотово. Обработано файлов: {len(files)}")


if __name__ == '__main__':
    main()