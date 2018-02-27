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


main = Blueprint('weekly', __name__)


@main.route('/', methods=['GET'])
def weekly_index():
    topic = Board.get_all_board()
    weekly = Weekly.get_all_note()
    return render_template('weekly/index.html', board=topic, weekly=weekly)


@main.route('/new', methods=['GET'])
def new():
    # 返回话题列表
    topic = list(Board.get_all_board())
    return render_template('new.html', board=topic)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    user_id = current_user_id()
    # board_id = get_board_id(title=form.get('board_id', '-1'))
    note = Weekly(form, user_id=user_id)
    Weekly._add(note)
    return '<h1> add ok</h1>'