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

main = Blueprint('index', __name__)


# 根据session得到当前的用户
def current_user():
    cur = session.get('user_name', '')
    return cur


@main.route('/', methods=['GET', 'POST'])
def index():
    u = session.get('user_name', '')
    return 'hello {}'.format(u)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username', '')
        password = request.form.get('password', '')
        if User.validate(name, password):
            session['user_name'] = name
            return redirect(url_for('index.index')) # 登录成功
        else:
            flash('找不到用户名')
    return render_template('login.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        u = User(form)
        User._add(u)
        return redirect(url_for('index.index'))
    return render_template('register.html')

