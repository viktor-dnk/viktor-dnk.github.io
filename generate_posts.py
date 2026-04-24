import os
import re
import yaml
from datetime import datetime

COLLECTIONS = ['_toponymy', '_info', '_mysteries-dolmens']
POSTS_DIR = '_posts'

def parse_front_matter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None, None
    fm = yaml.safe_load(match.group(1))
    body = content[match.end():]
    return fm, body

def slugify(title):
    # простой слаг из оригинального имени файла (без даты)
    return os.path.splitext(os.path.basename(title))[0]

def main():
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)
    # удаляем старые сгенерированные посты, чтобы не было дублей
    for f in os.listdir(POSTS_DIR):
        os.remove(os.path.join(POSTS_DIR, f))

    for col_dir in COLLECTIONS:
        if not os.path.isdir(col_dir):
            continue
        for fname in os.listdir(col_dir):
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(col_dir, fname)
            fm, body = parse_front_matter(fpath)
            if fm is None or 'date' not in fm or 'title' not in fm or 'description' not in fm:
                continue
            # извлекаем коллекцию из имени папки (например, _toponymy -> toponymy)
            collection = col_dir.lstrip('_')
            # слаг из имени исходного файла (убираем расширение)
            slug = os.path.splitext(fname)[0]
            # если имя файла содержит дату, то удаляем её префикс (YYYY-MM-DD-),
            # чтобы слаг был чистым названием
            date_match = re.match(r'\d{4}-\d{2}-\d{2}-(.+)', slug)
            if date_match:
                slug = date_match.group(1)
            # дата из front matter
            date = fm['date']
            if isinstance(date, datetime):
                date_str = date.strftime('%Y-%m-%d')
            else:
                # если дата записана как строка, пытаемся распарсить
                try:
                    date_str = datetime.strptime(str(date), '%Y-%m-%d').strftime('%Y-%m-%d')
                except:
                    # fallback: сегодня
                    date_str = datetime.now().strftime('%Y-%m-%d')
            # формируем имя файла поста
            post_filename = f"{date_str}-{slug}.md"
            post_path = os.path.join(POSTS_DIR, post_filename)
            # создаём содержимое
            description = fm['description'].replace('"', '\\"')
            # собираем front matter поста
            post_fm = {
                'layout': 'post',
                'title': fm['title'],
                'description': fm['description'],
                'date': fm['date'],
                'share-title': fm.get('share-title', fm['title']),
                'share-description': fm.get('share-description', fm['description']),
                'thumbnail-caption': fm.get('thumbnail-caption', ''),
                'collection': collection,
                'slug': slug,
                'permalink': f"/{collection}/{slug}/",   # удобный URL
                'categories': fm.get('category', []),     # можно добавить
                'keywords': fm.get('keywords', ''),
            }
            # записываем
            with open(post_path, 'w', encoding='utf-8') as out:
                out.write('---\n')
                yaml.dump(post_fm, out, allow_unicode=True, default_flow_style=False)
                out.write('---\n')
                out.write(description)   # содержимое поста = description
    print("Posts generated successfully.")

if __name__ == '__main__':
    main()