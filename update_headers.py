import os
import re
import sys
import glob

# 1. Получаем путь из аргументов командной строки
# Если не передан, используем путь по умолчанию
if len(sys.argv) > 1:
    search_pattern = sys.argv[1]
else:
    search_pattern = "_toponymy/2021/*.md"  # Значение по умолчанию
    print(f"Путь не указан. Используем по умолчанию: {search_pattern}")
    print(f"Что указать свой путь, запустите: python update_headers.py _toponymy/2021/*.md\n")

# 2. Регулярка для извлечения слага из cover-img
# Ищет путь вида /img/toponymy/INDIUK/cover.jpg
IMG_PATTERN = re.compile(r'/img/toponymy/([^/]+)/cover\.jpg')

# 3. Регулярка для поиска и замены строки head-extra
HEAD_EXTRA_PATTERN = re.compile(r'^(head-extra:\s*\[)(.*?)(\]\s*)$', re.MULTILINE)

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Ошибка чтения {filepath}: {e}")
        return

    # 1. Ищем слаг (например, 'indiuk') в метаданных картинки
    img_match = IMG_PATTERN.search(content)
    if not img_match:
        return # Пропускаем файл, если нет картинки с ожидаемым путем
    
    slug = img_match.group(1)
    # Формируем имя нового файла
    new_include = f"etc/tp_micro_faq_{slug}.html"

    # 2. Обновляем head-extra
    def replace_head_extra(match):
        start = match.group(1) # "head-extra: ["
        middle = match.group(2) # содержимое списка
        end = match.group(3)    # "]"
        
        # Проверяем, нет ли уже такого файла в списке, чтобы не дублировать
        # Учитываем возможные кавычки
        if new_include in middle or f"'{new_include}'" in middle or f'"{new_include}"' in middle:
            return match.group(0)
        
        # Добавляем запятую, если список не пустой
        separator = ", " if middle.strip() else ""
        return f"{start}{middle}{separator}{new_include}{end}"

    new_content = HEAD_EXTRA_PATTERN.sub(replace_head_extra, content)

    # Записываем изменения, только если контент изменился
    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Обновлено: {filepath}")
        except Exception as e:
            print(f"Ошибка записи {filepath}: {e}")

# 4. Поиск файлов по маске
# Если пользователь ввел путь вида _toponymy/2021/*.md
files = glob.glob(search_pattern, recursive=True)

if not files:
    print(f"Файлы по маске '{search_pattern}' не найдены!")
    print("Проверьте правильность пути.")
    sys.exit(1)

print(f"Найдено файлов: {len(files)}\n")

# 5. Запуск обработки
for filepath in files:
    if filepath.endswith('.md'):
        process_file(filepath)

print("\nГотово!")