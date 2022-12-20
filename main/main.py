from flask import Blueprint, render_template, request
from functions import posts_list
import logging
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='basic.log', level=logging.INFO, encoding='utf-8')


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_posts():
    search_name = request.args.get('s')
    posts = posts_list()
    if not posts:
        return '<h1>Ошибка в открытии json файла</h1>'
    search_posts_list = [post for post in posts if search_name.lower() in post['content'].lower()]
    logging.info(f'Поиска записей по запросу "{search_name}"')
    return render_template('post_list.html', search_name=search_name, posts=search_posts_list)
