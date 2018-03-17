from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    flash,
    g,
    current_app
)
from models.users import User
from models.web_view import Web_View
from tools.utils import current_user_id, is_login
from tools.log import logger
from tools.pagination import Pagination
from models.board import Board
from models.weekly import Weekly
import os
import random, string


main = Blueprint('index', __name__)


@main.route('/', methods=['GET', 'POST'])
@is_login
def index():
    Web_View.incre_views()
    page = request.args.get('page', '1')
    total = Weekly.get_total_page_num()
    
    board_list = Board.get_all_obj(int(page))
    note = Weekly.get_all_obj(page)
    # 构造文章的分页对象
    pagination = Pagination(int(page), int(total))
    return render_template('index/index.html', board=board_list, note=note, pagination=pagination)


@main.route('/manager', methods=['GET', 'POST'])
@is_login
def avater_upload():
    if request.method == 'GET':
        return render_template('index/manager.html')
    else:
        file = request.files['file']
        file_name = file.filename
        ext = file_name.rsplit('.', 1)[1]  # 获取文件后缀
        file_dir = current_app.config['AVATER_IMG_PATH']
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        # 将文件名用随机字符串代替
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 12))
        save_name = salt + '.' + ext
        file.save(os.path.join(file_dir,str(save_name)))
        flash('上传头像成功', 'success')

        # 将头像信息写入User表
        user_id = current_user_id()
        User.update_avater(user_id, save_name)
    return redirect(url_for('index.index'))

#    返回指定页数的对象
@main.route('/page/<int:id>/', methods=['GET'])
def get_page(id):
    page = id
    total = Weekly.get_total_page_num()
    board_list = Board.get_all_obj(page)
    note = Weekly.get_all_obj(page)
    pagination = Pagination(int(page), int(total))
    return render_template('index/index.html', board=board_list, note=note, pagination=pagination, User=User)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.validate(request.form)
        if u is None:
            flash('找不到用户或密码错误', 'danger')
        else:
            session['user_id'] = u.id
            session['user_name'] = u.user_name
            logger.info('{} success login'.format(u.user_name))
            flash('登陆成功', 'success')
            return redirect(url_for('index.index'))  # 登录成功
    return render_template('index/login.html')


@main.route('/logout', methods=['GET'])
@is_login
def logout():
    if session['user_id'] and session['user_id'] is not None:
        logger.info('{} success logout'.format(session['user_name']))
        return redirect(url_for('index.login'))
    else:
        return flash('还未登录')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        u = User(form)
        # 验证用户是否合法
        if u.check_username_occupy():
            User.new(u)
            logger.info('{} success register'.format(u.user_name))
            flash('注册成功', 'success')
            return redirect(url_for('index.index'))
        else:
            flash('用户名被占用，请重新输入', 'warning')
    return render_template('index/register.html')

