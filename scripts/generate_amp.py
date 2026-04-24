# scripts/generate_amp.py
import os
import re
import shutil
from pathlib import Path

TARGET_COLLECTIONS = ['_toponymy', '_info', '_mysteries-dolmens']
AMP_OUTPUT_DIR = '_amp'

def process_file(filepath, collection_slug, output_filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Проверяем наличие frontmatter
    if not content.strip().startswith('---'):
        # Нет frontmatter — добавляем минимальный
        new_content = f'---\nlayout: amp\npermalink: /amp/{collection_slug}/{Path(filepath).stem}/\n---\n{content}'
    else:
        # Разделяем frontmatter и тело
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            # Невалидный frontmatter — копируем как есть с добавлением layout
            new_content = f'---\nlayout: amp\npermalink: /amp/{collection_slug}/{Path(filepath).stem}/\n---\n{content}'
        else:
            frontmatter, body = parts[1], parts[2]
            
            # Проверяем и обновляем/добавляем layout
            if not re.search(r'^layout:\s*', frontmatter, re.MULTILINE):
                frontmatter += 'layout: amp\n'
            else:
                frontmatter = re.sub(r'^layout:\s*.*$', 'layout: amp', frontmatter, flags=re.MULTILINE)
            
            # Проверяем и обновляем/добавляем permalink
            permalink_val = f'/amp/{collection_slug}/{Path(filepath).stem}/'
            if not re.search(r'^permalink:\s*', frontmatter, re.MULTILINE):
                frontmatter += f'permalink: {permalink_val}\n'
            else:
                frontmatter = re.sub(r'^permalink:\s*.*$', f'permalink: {permalink_val}', frontmatter, flags=re.MULTILINE)
            
            new_content = f'---\n{frontmatter}---\n{body}'

    # Создаём директорию и записываем файл
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    if os.path.exists(AMP_OUTPUT_DIR):
        shutil.rmtree(AMP_OUTPUT_DIR)
    os.makedirs(AMP_OUTPUT_DIR, exist_ok=True)

    for coll in TARGET_COLLECTIONS:
        coll_slug = coll.lstrip('_')
        src_path = Path(coll)
        dst_dir = Path(AMP_OUTPUT_DIR) / coll_slug

        if not src_path.is_dir():
            print(f"[WARN] Директория {src_path} не найдена, пропускаю.")
            continue

        for md_file in src_path.glob('*.md'):
            dst_file = dst_dir / md_file.name
            process_file(str(md_file), coll_slug, str(dst_file))
            print(f"[OK] Создана AMP-версия: {dst_file}")

if __name__ == '__main__':
    main()