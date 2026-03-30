import os
import re
import sys
import glob
from datetime import datetime

# 1. Получаем аргументы командной строки
if len(sys.argv) > 1:
    search_pattern = sys.argv[1]
else:
    search_pattern = "_toponymy/**/*.md"
    print(f"Путь не указан. Используем по умолчанию: {search_pattern}")

if len(sys.argv) > 2:
    new_date = sys.argv[2]
else:
    # Дата по умолчанию
    new_date = "2026-03-30 12:00:00 +0300"
    print(f"Дата не указана. Используем по умолчанию: {new_date}")
    print(f"Пример запуска: python update_date.py \"_toponymy/2021/*.md\" \"2026-03-30 12:00:00 +0300\"\n")

# 2. Регулярка для поиска поля last_modified_at
# Ловит строку вида: last_modified_at: 2021-01-04 23:00
DATE_PATTERN = re.compile(r'^(last_modified_at:\s*)(.+?)\s*$', re.MULTILINE)

def process_file(filepath, new_date_value):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Ошибка чтения {filepath}: {e}")
        return

    # Проверяем, есть ли вообще это поле в файле
    if not DATE_PATTERN.search(content):
        print(f"Пропущено (нет поля): {filepath}")
        return

    # Заменяем дату
    def replace_date(match):
        prefix = match.group(1)  # "last_modified_at: "
        return f"{prefix}{new_date_value}"

    new_content = DATE_PATTERN.sub(replace_date, content)

    # Записываем изменения, только если контент изменился
    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Обновлено: {filepath}")
        except Exception as e:
            print(f"Ошибка записи {filepath}: {e}")
    else:
        print(f"Без изменений: {filepath}")

# 3. Поиск файлов по маске
files = glob.glob(search_pattern, recursive=True)

if not files:
    print(f"Файлы по маске '{search_pattern}' не найдены!")
    print("Проверьте правильность пути.")
    sys.exit(1)

print(f"Найдено файлов: {len(files)}")
print(f"Новая дата: {new_date}\n")

# 4. Запуск обработки
for filepath in files:
    if filepath.endswith('.md'):
        process_file(filepath, new_date)

print("\nГотово!")