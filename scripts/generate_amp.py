# scripts/generate_amp.py
import os
import re
import shutil

# Коллекции, для которых нужно генерировать AMP
TARGET_COLLECTIONS = ['_toponymy', '_info', '_mysteries-dolmens']
AMP_OUTPUT_DIR = '_amp'

def process_file(filepath, collection_slug, output_filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Регулярка для поиска YAML frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    
    slug = os.path.splitext(os.path.basename(filepath))[0]
    permalink_path = f'/amp/{collection_slug}/{slug}/'

    if fm_match:
        frontmatter = fm_match.group(1)
        body = content[fm_match.end():]
        
        lines = frontmatter.splitlines()
        new_lines = []
        layout_updated = False
        permalink_updated = False

        for line in lines:
            stripped = line.strip()
            if stripped.startswith('layout:'):
                new_lines.append('layout: amp')
                layout_updated = True
            elif stripped.startswith('permalink:'):
                new_lines.append(f'permalink: {permalink_path}')
                permalink_updated = True
            else:
                new_lines.append(line)

        if not layout_updated:
            new_lines.append('layout: amp')
        if not permalink_updated:
            new_lines.append(f'permalink: {permalink_path}')

        new_frontmatter = '\n'.join(new_lines)
        new_content = f'---\n{new_frontmatter}\n---\n{body}'
    else:
        # Если frontmatter отсутствует, создаём его
        new_content = f'---\nlayout: amp\npermalink: {permalink_path}\n---\n{content}'

    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    if os.path.exists(AMP_OUTPUT_DIR):
        shutil.rmtree(AMP_OUTPUT_DIR)

    for coll in TARGET_COLLECTIONS:
        coll_slug = coll.lstrip('_')
        src_path = coll
        dst_dir = os.path.join(AMP_OUTPUT_DIR, coll_slug)

        if not os.path.isdir(src_path):
            print(f"[WARN] Директория {src_path} не найдена, пропускаю.")
            continue

        for filename in os.listdir(src_path):
            if filename.endswith('.md'):
                src_file = os.path.join(src_path, filename)
                dst_file = os.path.join(dst_dir, filename)
                process_file(src_file, coll_slug, dst_file)
                print(f"[OK] Создана AMP-версия: {dst_file}")

if __name__ == '__main__':
    main()