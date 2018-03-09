from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    g,
    jsonify,
    make_response,
    current_app,
)
from models.weekly import Weekly
from models.board import Board
from models.users import User
from models.conmments import Comments
from tools.utils import current_user_id, is_login
from tools.log import logger
import os, datetime


main = Blueprint('weekly', __name__)


@main.route('/new', methods=['GET'])
@is_login
def new():
    # 返回话题列表
    logger.info('新建文件')
    topic = Board.get_all_obj()
    return render_template('weekly/new.html', board=topic)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    user_id = current_user_id()
    note = Weekly(form, user_id=user_id)
    Weekly.new(note)
    return redirect(url_for('index.index'))


@main.route('/detail/<id>')
def detail(id):
    note = Weekly.find_by_id(id)
    if note is not None:
        note.incre_views()
    else:
        logger.error('get_obj_by_id is None')
  
    # 根据用户Id，查找作者
    author = User.find_by_id(current_user_id()).user_name
    
    # 根据文章id，查找其所有评论
    comments = Comments.find_by_note_id(id)
    return render_template('weekly/detail.html', note=note, comments=comments, author=author)


@main.route('/detail/<id>/add_commit', methods=['POST'])
@is_login
def add_comment(id):
    content = request.form.get('content', 'null')
    
    # 文章的评论数加1
    note = Weekly.find_by_id(id)
    if note is not None:
        note.incre_replys()
    
    obj = Comments(content, current_user_id(), id)
    Comments.new(obj)
    return redirect(url_for('weekly.detail', id=id))


# 接收editormd中ajax发送的图片，保存到本地，并返回链接
@main.route('/img', methods=['POST'])
def upload_img():
    file = request.files.get('editormd-image-file')
    if not file:
        res = {
            'success': 0,
            'message': u'图片为空或格式错误'
        }
        return jsonify(res)
    else:
        ex = os.path.splitext(file.filename)[1]
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ex
        file.save(os.path.join(current_app.config['IMG_PATH'], filename))
        res = {
            'success' : 1,
            'message' : u'success',
            'url' : url_for('weekly.get_img', filename=filename)
        }
        return jsonify(res)


# 返回图片， TODO: nginx缓存
@main.route('/image/<filename>', methods=['GET', 'POST'])
def get_img(filename):
    with open(os.path.join(current_app.config['IMG_PATH'], filename), 'rb') as file:
        r = make_response(file.read())
        return r
        