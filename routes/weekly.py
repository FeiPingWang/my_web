from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
)
from models.weekly import Weekly
from models.board import Board
from models.users import User
from models.conmments import Comments
from tools.utils import current_user_id
from tools.log import logger
from models.users import new_session


main = Blueprint('weekly', __name__)


@main.route('/new', methods=['GET'])
def new():
    # 返回话题列表
    topic = Board.get_all_board()
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
    
    # 增加浏览次数一次
    session, obj = Weekly.get_obj_by_id(id)
    if obj is not None:
        obj.views += 1
    else:
        logger.error('get_obj_by_id is None')
    
    print('obj.id ', obj.id)
    # 根据用户Id，查找作者
    author = session.query(User.user_name).filter(User.id == obj.user_id).first()
    session.commit()
    session.close()
    
    # 根据文章id，查找其所有评论
    comments = Comments.find_by_note_id(id)
    return render_template('weekly/detail.html', note=note, comments=comments, author=author[0])


@main.route('/detail/<id>/add_commit', methods=['POST'])
def add_comment(id):
    content = request.form.get('content', 'null')
    user_id = current_user_id()
    
    obj = Comments(content, user_id, id)
    Comments.new(obj)
    return redirect(url_for('weekly.detail', id=id))