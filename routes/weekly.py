from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    g,
    jsonify,
    flash,
    make_response,
    current_app,
)
from models.weekly import Weekly
from models.users import User
from models.conmments import Comments
from models.web_view import Web_View
from models.types import Types
from models.menus import Menus
from tools.utils import current_user_id, is_login
from tools.log import logger
import os, datetime


main = Blueprint('weekly', __name__)


@main.route('/new', methods=['GET'])
@is_login
def new():
    # 返回话题列表
    logger.info('新建文件')
    # TODO；需要优化
    topic = g.my_session.query(Types).all()
    print(topic)
    return render_template('weekly/new.html', board=topic)


@main.route('/add', methods=['POST'])
@is_login
def add():
    form = request.form
    user_id = current_user_id()
    note = Weekly(form, user_id=user_id)
    Weekly.new(note)
    flash('发表文章成功', 'success')
    logger.info('add new note id<{}> title<{}>'.format(note.id, note.title))
    return redirect(url_for('index.index'))


@main.route('/detail/<id>/')
def detail(id):
    Web_View.incre_views()
    note = Weekly.find_by_id(id)
    if note is not None:
        note.incre_views()
    else:
        logger.error('get_obj_by_id is None')
  
    # 根据用户Id，查找作者
    author = User.find_by_id(note.user_id).user_name
    
    # 根据文章id，查找其所有评论
    comments = Comments.get_obj_by_filter(note_id=id)
    return render_template('weekly/detail.html', note=note, comments=comments, author=author)


@main.route('/delete/<id>')
@is_login
def delete(id):
    note = Weekly.find_by_id(id)
    title = note.title
    logger.info('note {} delete success'.format(title))
    Weekly.delete(note)
    return redirect(url_for('index.index'))
    

@main.route('/edit/<id>', methods=['GET', 'POST'])
@is_login
def edit(id):
    old_note = Weekly.find_by_id(id)
    content = request.form.get('content', '')
    # 如果为空字符串，表示还没有提交更改
    if content is '':
        topic = Types.get_obj_by_filter()
        author = User.find_by_id(old_note.user_id).user_name
        comments = Comments.get_obj_by_filter(note_id=id)
        return render_template('weekly/edit.html', note=old_note, comments=comments, author=author, board=topic)
    else:
        # 更新数据库
        new_note = Weekly(request.form, old_note.user_id)
        Weekly.update(old_note, new_note)
        return redirect(url_for('weekly.detail', id=id))


@main.route('/detail/add_commit/<id>', methods=['POST'])
@is_login
def add_comment(id):
    content = request.form.get('content', 'null')
    
    # 文章的评论数加1
    note = Weekly.find_by_id(id)
    if note is not None:
        note.incre_replys()
    
    obj = Comments(content, current_user_id(), id)
    Comments.new(obj)
    logger.info('note<{}> add comment '.format(id))
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
        logger.info('save img {}'.format(filename))
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
        