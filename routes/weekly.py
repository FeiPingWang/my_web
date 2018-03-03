from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    flash,
)
from models.weekly import Weekly
from models.board import Board
from tools.utils import current_user_id
from tools.log import logger


main = Blueprint('weekly', __name__)


@main.route('/', methods=['GET'])
def weekly_index():
    topic = Board.get_all_board()
    weekly = Weekly.get_all_note()
    return render_template('weekly/index.html', board=topic, weekly=weekly)


@main.route('/new', methods=['GET'])
def new():
    # 返回话题列表
    topic = Board.get_all_board()
    logger.info('board list: ', topic)
    return render_template('new.html', board=topic)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    user_id = current_user_id()
    note = Weekly(form, user_id=user_id)
    Weekly._add(note)
    return redirect(url_for('weekly.weekly_index'))