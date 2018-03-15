from flask import (
    Flask,
    Blueprint,
    g,
)


main = Blueprint('test', __name__)


@main.route('/api')
def api():
    return '<h1>Hello World</h1>'