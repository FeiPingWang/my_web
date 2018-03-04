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
from tools.utils import current_user_id
from models.board import Board
from models.weekly import Weekly


main = Blueprint('index', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    u = current_user_id()
    if u == 'null':   # 未登陆
        return redirect(url_for('index.login'))
    else:
        board_list = Board.get_all_obj()
        note = Weekly.get_all_obj()
        # print('note ', note)
        return render_template('index/index.html', board=board_list, note=note)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.validate(request.form)
        if u is None:
            flash('找不到用户名')
        else:
            session['user_id'] = u.id   # u[0] is user_id
            session['user_name'] = u.user_name
            return redirect(url_for('index.index'))  # 登录成功
    return render_template('index/login.html')


@main.route('/logout', methods=['GET'])
def logout():
    if session['user_id'] and session['user_id'] is not None:
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

