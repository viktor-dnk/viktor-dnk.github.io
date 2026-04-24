# scripts/generate_amp.py
import os
import shutil
from pathlib import Path
import yaml

TARGET_COLLECTIONS = ['_toponymy', '_info', '_mysteries-dolmens']
AMP_OUTPUT_DIR = '_amp'

def process_file(filepath, collection_slug, output_filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Разделяем frontmatter и тело
    if not content.strip().startswith('---'):
        # Нет frontmatter — создаём минимальный
        fm = {'layout': 'amp', 'permalink': f'/amp/{collection_slug}/{Path(filepath).stem}/', 'published': True}
        new_content = f'---\n{yaml.dump(fm, allow_unicode=True, sort_keys=False)}---\n{content}'
    else:
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            # Невалидный frontmatter — копируем как есть + добавляем поля
            fm = {'layout': 'amp', 'permalink': f'/amp/{collection_slug}/{Path(filepath).stem}/', 'published': True}
            new_content = f'---\n{yaml.dump(fm, allow_unicode=True, sort_keys=False)}---\n{content}'
        else:
            # Парсим YAML
            try:
                fm = yaml.safe_load(parts[1])
            except yaml.YAMLError:
                # Если не распарсилось — добавляем поля текстом
                frontmatter = parts[1]
                if 'layout:' not in frontmatter:
                    frontmatter += 'layout: amp\n'
                if 'permalink:' not in frontmatter:
                    frontmatter += f"permalink: /amp/{collection_slug}/{Path(filepath).stem}/\n"
                if 'published:' not in frontmatter:
                    frontmatter += 'published: true\n'
                new_content = f'---\n{frontmatter}---\n{parts[2]}'
            else:
                # Обновляем поля
                fm['layout'] = 'amp'
                fm['permalink'] = f'/amp/{collection_slug}/{Path(filepath).stem}/'
                fm['published'] = True
                body = parts[2]
                # Собираем обратно: sort_keys=False сохраняет порядок, allow_unicode=True для кириллицы
                new_content = f'---\n{yaml.dump(fm, allow_unicode=True, sort_keys=False)}---\n{body}'

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