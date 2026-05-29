# -*- coding: utf-8 -*-
import os
import re
import sys
import yaml
import tempfile
import subprocess
from bs4 import BeautifulSoup
"""python update_iptc_copyright_one_md.py "D:\work\tmp\gh\viktor-dnk.github.io\_toponymy\2026\2026-02-24-volkonka.md" """
def find_exiftool():
    """Автоматический поиск исполняемого файла ExifTool в указанной папке"""
    exiftool_dir = r"D:\work\tmp\ExifTool"
    if not os.path.exists(exiftool_dir):
        return None
    for f in os.listdir(exiftool_dir):
        if f.lower().startswith('exiftool') and f.lower().endswith('.exe'):
            return os.path.join(exiftool_dir, f)
    return os.path.join(exiftool_dir, "exiftool.exe")

def process_article(md_path):
    exiftool_exe = find_exiftool()
    if not exiftool_exe or not os.path.exists(exiftool_exe):
        print(f"❌ Ошибка: ExifTool не найден в папке D:\\work\\tmp\\ExifTool")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Парсинг Frontmatter (шапки)
    lines = content.split('\n')
    fm_lines = []
    start_idx = 0
    if lines and lines[0].strip() == '---':
        start_idx = 1
    
    for i in range(start_idx, len(lines)):
        if lines[i].strip() == '---':
            break
        fm_lines.append(lines[i])
        
    fm_text = '\n'.join(fm_lines)
    keywords_str = ""
    
    try:
        fm = yaml.safe_load(fm_text)
        if isinstance(fm, dict):
            kw_val = fm.get('keywords', '')
            if isinstance(kw_val, list):
                keywords_str = ", ".join(kw_val)
            else:
                keywords_str = str(kw_val)
    except Exception:
        # Фоллбэк на случай невалидного YAML
        match = re.search(r'^keywords:\s*(.*?)$', fm_text, re.MULTILINE)
        if match:
            keywords_str = match.group(1)
            
    keywords_list = [k.strip() for k in keywords_str.split(',') if k.strip()]
    
    # 2. Определение категории и названия статьи
    filename = os.path.basename(md_path)
    article_name = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename).replace('.md', '')
    
    if '_toponymy' in md_path.replace('\\', '/'):
        category = 'toponymy'
    elif '_mysteries-dolmens' in md_path.replace('\\', '/'):
        category = 'mysteries-dolmens'
    else:
        category = 'unknown'
        
    source_url = f"https://viktor-dnk.ru/{category}/{article_name}/"
    
    parts = md_path.replace('\\', '/').split('/')
    try:
        root_idx = parts.index('viktor-dnk.github.io')
        base_dir = '/'.join(parts[:root_idx+1])
    except ValueError:
        print("❌ Ошибка: Не удалось определить корневую папку 'viktor-dnk.github.io' в пути к файлу.")
        return

    # 3. Парсинг HTML-тегов для поиска изображений
    soup = BeautifulSoup(content, 'html.parser')
    figures = soup.find_all('figure')
    
    processed_count = 0
    
    for figure in figures:
        # Проверяем наличие метатегов авторского права
        has_copyright = (
            figure.find('meta', attrs={'itemprop': 'license'}) is not None or
            figure.find('meta', attrs={'itemprop': 'copyrightNotice'}) is not None or
            figure.find(attrs={'itemtype': 'https://schema.org/ImageObject'}) is not None
        )
        
        if not has_copyright:
            continue
            
        img_tag = figure.find('img')
        if not img_tag:
            continue
            
        img_src = img_tag.get('src', '').strip()
        if not img_src:
            continue
            
        a_tag = figure.find('a')
        title = ""
        if a_tag and a_tag.get('title'):
            title = a_tag.get('title').strip()
        elif img_tag.get('title'):
            title = img_tag.get('title').strip()
        elif img_tag.get('alt'):
            title = img_tag.get('alt').strip()
            
        figcaption = figure.find('figcaption')
        caption = figcaption.get_text(" ", strip=True) if figcaption else ""
        
        img_rel_path = img_src.lstrip('/')
        img_abs_path = os.path.join(base_dir, img_rel_path).replace('/', os.sep)
        
        if not os.path.exists(img_abs_path):
            print(f"⚠️ Предупреждение: Изображение не найдено на диске: {img_abs_path}")
            continue
            
        print(f"-> Обработка: {os.path.basename(img_abs_path)}")
        
        # 4. Формирование аргументов для ExifTool (Только XMP + Очистка IPTC)
        args = [
            "-overwrite_original",
            "-charset", "exiftool=utf8",
            "-IPTC:all=",  # Полностью очищаем устаревший IPTC блок
            "-XMP:all=",
            
            # === XMP (Современный стандарт, UTF-8, нет лимитов длины) ===
            "-XMP-xmpRights:Marked=True"
            "-XMP-xmpRights:WebStatement=https://viktor-dnk.ru/info/copyright/"
            f"-XMP:Title={title}",
            f"-XMP:Headline={title}",
            f"-XMP:Description={caption}",
            "-XMP:Creator=Ковешников В.Н.",
            "-XMP:Writer-Editor=Ковешников В.Н.", # Заполняем Writer-Editor
            f"-XMP:AuthorsPosition={title}",
            f"-XMP:Rights=https://viktor-dnk.ru/info/copyright/",
            f"-XMP:Source={source_url}",
            "-XMP:Location=Кубань",
            "-XMP:State=Краснодарский край",
            "-XMP:Country=Россия",
            "-XMP:Credit=Заметки географа",
        ]
        
        # Ключевые слова (Keywords) пишем только в XMP Subject
        for kw in keywords_list:
            args.append(f"-XMP:Subject+={kw}")
            
        # Запись аргументов во временный файл
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', delete=False, suffix='.txt') as f:
            args_file = f.name
            for arg in args:
                f.write(arg + '\n')
                
        cmd = [exiftool_exe, "-@", args_file, img_abs_path]
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processed_count += 1
        except subprocess.CalledProcessError as e:
            err_msg = e.stderr.decode('utf-8', errors='ignore') if e.stderr else str(e)
            print(f"❌ Ошибка ExifTool для {img_abs_path}: {err_msg}")
        finally:
            os.unlink(args_file)
            
    print(f"\n✅ Готово! Обновлено изображений: {processed_count}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_md = sys.argv[1]
        if os.path.exists(target_md):
            process_article(target_md)
        else:
            print(f"❌ Файл не найден: {target_md}")
    else:
        print("Использование: python update_iptc.py <путь_к_файлу.md>")