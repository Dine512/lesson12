import json


def posts_list():
    try:
        with open('posts.json', 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts
    except FileNotFoundError:
        return False


def append_post(_dict):
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(_dict, file, ensure_ascii=False, indent=4)
