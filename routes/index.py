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


main = Blueprint('index', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    u = current_user_id()
    if u == 'null':   # 未登陆
        return redirect(url_for('index.login'))
    else:
        board_list = Board.get_all_board()
        return render_template('index.html', board=board_list)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.validate(request.form)
        if u is None:
            flash('找不到用户名')
        else:
            session['user_id'] = u[0]   # u[0] is user_id
            return redirect(url_for('index.index'))  # 登录成功
    return render_template('login.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        u = User(form)
        print('password ', u.password)
        User._add(u)
        return redirect(url_for('index.index'))
    return render_template('register.html')

