from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    flash,
)
from models.users import User
from tools.utils import current_user_id, is_login
from tools.log import logger
from tools.pagination import Pagination
from models.board import Board
from models.weekly import Weekly


main = Blueprint('index', __name__)


@main.route('/', methods=['GET', 'POST'])
@is_login
def index():
    page = request.args.get('page', '1')
    total = Weekly.get_total_page_num()
    
    board_list = Board.get_all_obj(int(page))
    note = Weekly.get_all_obj(page)

    # 构造文章的分页对象
    pagination = Pagination(int(page), int(total))
    return render_template('index/index.html', board=board_list, note=note, pagination=pagination)
    
#    返回指定页数的对象
@main.route('/page/<int:id>/', methods=['GET'])
def get_page(id):
    page = id
    total = Weekly.get_total_page_num()
    board_list = Board.get_all_obj(page)
    note = Weekly.get_all_obj(page)
    pagination = Pagination(int(page), int(total))
    return render_template('index/index.html', board=board_list, note=note, pagination=pagination)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.validate(request.form)
        if u is None:
            flash('找不到用户名')
        else:
            session['user_id'] = u.id   # u[0] is user_id
            session['user_name'] = u.user_name
            logger.info('{} success login'.format(u.user_name))
            return redirect(url_for('index.index'))  # 登录成功
    return render_template('index/login.html')


@main.route('/logout', methods=['GET'])
@is_login
def logout():
    if session['user_id'] and session['user_id'] is not None:
        logger.info('{} success logout'.format(session['user_name']))
        session.pop('user_id')
        session.pop('user_name')
        return redirect(url_for('index.login'))
    else:
        return flash('还未登录')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        u = User(form)
        User.new(u)
        return redirect(url_for('index.index'))
    return render_template('index/register.html')

