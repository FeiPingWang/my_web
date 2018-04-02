from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    flash,
    g,
    current_app,
    jsonify,
    make_response
)
from models.users import User
from models.web_view import Web_View
from models.types import Types
from tools.utils import current_user_id, is_login
from tools.log import logger
from tools.pagination import Pagination
from models.weekly import Weekly
import os
import random, string


main = Blueprint('index', __name__)


@main.route('/', methods=['GET', 'POST'])
@is_login
def index():
    Web_View.incre_views()
    page = request.args.get('page', '1', type=int)
    note = Weekly.get_all_obj_by_page(page=page)

    total_num = len(Weekly.get_obj_by_filter())

    total_page = Pagination.get_total_page_num(total_num)

    # 构造文章的分页对象
    pagination = Pagination(int(page), total_page)
    return render_template('index/index.html', note=note, pagination=pagination, endpoint='index.index')


# 根据文章分类，显示文章
@main.route('/note_type/<int:id>')
def note_type(id):
    Web_View.incre_views()
    page = request.args.get('page', '1')
    # 指定分类的所有文章
    note = Weekly.get_all_obj_by_page(page=page, type_id=id)
    # 返回分页对象
    total_num = len(Weekly.get_obj_by_filter(type_id=id))
    total_page = Pagination.get_total_page_num(total_num)
    pagination = Pagination(int(page), total_page)
    return render_template('index/index.html', note=note, pagination=pagination, endpoint='index.note_type', id=id)


@main.route('/person_info', methods=['GET', 'POST'])
@is_login
def person_info():
    if request.method == 'GET':
        u = User.find_by_id(current_user_id())
        return render_template('index/person_info.html', user=u)
    else:
        file = request.files['file']
        file_name = file.filename
        print('file_name, ', file_name)
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
            return redirect(url_for('index.login'))
        else:
            flash('用户名被占用，请重新输入', 'warning')
    return render_template('index/register.html')


@main.route('/testhttp', methods=['GET', 'POST'])
def testhttp():
    if request.method == 'GET':
        result = make_response(render_template('test_http.html'))
        result.headers['test_header'] = "wfp"
        return result
    else:
        header = request.headers.get("test_header")
        data = jsonify({'result':'ok', 'header': header})
        return data
    return '<h1>success</h1>'