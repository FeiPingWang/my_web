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
from tools.utils import current_user_id


main = Blueprint('weekly', __name__)


@main.route('/', methods=['GET'])
def weekly_index():
    return '<h1> topic </h1>'


@main.route('/new', methods=['GET'])
def new():
    return render_template('new.html', bs=['1','2','3'])


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    user_id = current_user_id()
    # board_id = get_board_id(title=form.get('board_id', '-1'))
    note = Weekly(form, user_id=user_id)
    Weekly._add(note)
    return '<h1> add ok</h1>'