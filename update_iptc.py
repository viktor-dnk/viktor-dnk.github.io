# -*- coding: utf-8 -*-
import os
import re
import sys
import yaml
import tempfile
import subprocess
from bs4 import BeautifulSoup
from datetime import datetime

# === НАСТРОЙКИ ПУТЕЙ ===
# Базовая директория вашего репозитория. 
# По умолчанию берется папка, в которой лежит сам скрипт.
# Если вы кладете скрипт в корень viktor-dnk.github.io, ничего менять не нужно.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXIFTOOL_DIR = r"D:\work\tmp\ExifTool"
# =======================

def find_exiftool():
    if not os.path.exists(EXIFTOOL_DIR):
        return None
    for f in os.listdir(EXIFTOOL_DIR):
        if f.lower().startswith('exiftool') and f.lower().endswith('.exe'):
            return os.path.join(EXIFTOOL_DIR, f)
    return os.path.join(EXIFTOOL_DIR, "exiftool.exe")

def get_all_articles():
    """Собирает пути ко всем статьям в нужных папках"""
    paths = []
    
    # 1. Папка _mysteries-dolmens
    myst_dir = os.path.join(BASE_DIR, "_mysteries-dolmens")
    if os.path.exists(myst_dir):
        for f in os.listdir(myst_dir):
            if f.endswith('.md'):
                paths.append(os.path.join(myst_dir, f))
                
    # 2. Папка _toponymy по годам (2021-2026)
    for year in range(2021, 2027):
        topo_dir = os.path.join(BASE_DIR, "_toponymy", str(year))
        if os.path.exists(topo_dir):
            for f in os.listdir(topo_dir):
                if f.endswith('.md'):
                    paths.append(os.path.join(topo_dir, f))
                    
    return paths

def update_last_modified(md_path, new_date_str):
    """Обновляет тег last_modified_at в frontmatter markdown файла"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Паттерн 1: Ищем существующий last_modified_at и заменяем его
    pattern = re.compile(r'^(---\s*\n.*?)(last_modified_at:\s*.*?)(\n.*?\n---)', re.MULTILINE | re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(rf'\1last_modified_at: {new_date_str}\3', content, count=1)
    else:
        # Паттерн 2: Если тега нет, добавляем его сразу после тега date:
        date_pattern = re.compile(r'^(---\s*\n.*?)(date:\s*.*?\n)(.*?\n---)', re.MULTILINE | re.DOTALL)
        if date_pattern.search(content):
            new_content = date_pattern.sub(rf'\1\2last_modified_at: {new_date_str}\n\3', content, count=1)
        else:
            return False
            
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def process_article(md_path, new_date_str):
    exiftool_exe = find_exiftool()
    if not exiftool_exe:
        print(f"❌ Ошибка: ExifTool не найден в папке {EXIFTOOL_DIR}")
        return 0

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Парсинг Frontmatter
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
        base_dir = BASE_DIR

    # 3. Парсинг HTML
    soup = BeautifulSoup(content, 'html.parser')
    figures = soup.find_all('figure')
    
    processed_count = 0
    
    for figure in figures:
        has_copyright = (
            figure.find('meta', attrs={'itemprop': 'license'}) is not None or
            figure.find('meta', attrs={'itemprop': 'copyrightNotice'}) is not None or
            figure.find(attrs={'itemtype': 'https://schema.org/ImageObject'}) is not None
        )
        
        if not has_copyright:
            continue
            
        img_tag = figure.find('img')
        if not img_tag: continue
            
        img_src = img_tag.get('src', '').strip()
        if not img_src: continue
            
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
            continue
            
        args = [
            "-overwrite_original",
            "-charset", "exiftool=utf8",
            "-IPTC:all=",
            "-XMP-xmpRights:Marked=True",
            "-XMP-xmpRights:WebStatement=https://viktor-dnk.ru/info/copyright/",
            f"-XMP:Title={title}",
            f"-XMP:Headline={title}",
            f"-XMP:Description={caption}",
            "-XMP:Creator=Ковешников В.Н.",
            "-XMP:Writer-Editor=Ковешников В.Н.",
            f"-XMP:AuthorsPosition={title}",
            f"-XMP:Rights=https://viktor-dnk.ru/info/copyright/",
            f"-XMP:Source={source_url}",
            "-XMP:Location=Краснодарский край",
            "-XMP:State=Краснодарский край",
            "-XMP:Country=Россия",
            "-XMP:Credit=Заметки географа",
        ]
        
        for kw in keywords_list:
            args.append(f"-XMP:Subject+={kw}")
            
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
            
    # Обновляем дату в шапке только если были обновлены изображения
    if processed_count > 0:
        if update_last_modified(md_path, new_date_str):
            print(f"📅 Обновлено last_modified_at в {filename}")
            
    return processed_count

def main():
    # Округляем текущее время до целого часа в минус (например, 14:45 -> 14:00)
    now = datetime.now()
    rounded_time = now.replace(minute=0, second=0, microsecond=0)
    new_date_str = rounded_time.strftime("%Y-%m-%d %H:00 +0300")
    
    print(f"🕒 Время для last_modified_at: {new_date_str}")
    
    articles = get_all_articles()
    if not articles:
        print("⚠️ Не найдено ни одной статьи для обработки. Проверьте BASE_DIR.")
        return
        
    print(f"🔍 Найдено статей для анализа: {len(articles)}\n")
    
    total_updated_images = 0
    updated_articles_count = 0
    
    for md_path in articles:
        print(f"--- Обработка: {os.path.basename(md_path)} ---")
        count = process_article(md_path, new_date_str)
        if count > 0:
            print(f"✅ Обновлено изображений: {count}")
            total_updated_images += count
            updated_articles_count += 1
        else:
            print("ℹ️ Изображений с копирайтом не найдено.")
            
    print(f"\n🏁 ИТОГО:")
    print(f"Статей с обновленными метаданными: {updated_articles_count}")
    print(f"Всего обработано изображений: {total_updated_images}")

if __name__ == "__main__":
    # Поддержка гибридного режима: 
    # Если передан аргумент - обрабатываем только его (для отладки)
    # Если без аргументов - обходим все папки
    if len(sys.argv) > 1:
        target_md = sys.argv[1]
        if os.path.exists(target_md):
            now = datetime.now().replace(minute=0, second=0, microsecond=0)
            process_article(target_md, now.strftime("%Y-%m-%d %H:00 +0300"))
        else:
            print(f"❌ Файл не найден: {target_md}")
    else:
        main()