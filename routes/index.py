from flask import (
    Blueprint,
    render_template,
    session,
    request,
)

main = Blueprint('index', __name__)


# 根据session得到当前的用户
def current_user():
    cur = session.get('user_name', '')
    return cur


@main.route('/', methods=['GET', 'POST'])
def index():
    u = session.get('user_name', '')
    # if u != 'wfp':
    return render_template('login.html')
    # return 'hello {}'.format(u)


@main.route('/login', methods=['GET', 'POST'])
def login():
    u = request.form.get('name')
    session['user_name'] = u
    return '<h1>success</h1>'


@main.route('/register', methods=['GET', 'POST'])
def register():
    pass
