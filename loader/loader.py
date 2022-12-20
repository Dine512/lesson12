from flask import Blueprint, render_template, request
from functions import posts_list, append_post
import logging
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO, encoding='utf-8')


@loader_blueprint.route('/post_create')
def post_create():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post():

    content = request.form['content']
    picture = request.files.get('picture')
    if picture:
        filename = picture.filename
        if not filename.split('.')[-1] in ['png', 'jpeg']:
            logging.info('Загруженный файл не кратинка')
            return '<h1>Загруженный файл не кратинка</h1>'
        picture.save(f'./static/images/{filename}')
        post_dict = {'content': content, 'pic': f'/static/images/{filename}'}
        json_list = posts_list()
        json_list.append(post_dict)
        append_post(json_list)
        return render_template('post_uploaded.html', picture=f'/static/images/{filename}', content=content)
    else:
        logging.error('Ошибка загрузки')
        return '<h1>Ошибка загрузки</h1>'


