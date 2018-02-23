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
from routes.index import current_user


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
    u = current_user()
    note = Weekly(form, user_id=1)
    Weekly._add(note)
    return '<h1> add ok</h1>'