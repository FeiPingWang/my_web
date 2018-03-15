from flask import Flask, g
from tools.orm import Session
from app_config import Config


app = Flask(__name__)
app.config.from_object(Config)


from routes.index import main as index_routes
from routes.weekly import main as weekly_routes
from routes.test import main as test_routes


app.register_blueprint(index_routes)
app.register_blueprint(weekly_routes, url_prefix='/weekly')
app.register_blueprint(test_routes, url_prefix='/test')


from models.users import User
from models.web_view import Web_View
from models.board import Board
from models.weekly import Weekly
from models.conmments import Comments


# 把dict中的变量加入到jinja2的上下文，在所有模板中都可见
@app.context_processor
def all_modules():
    return dict(User=User,
                Board=Board,
                Weekly=Weekly,
                Web_View=Web_View,
                Comments=Comments,
                )


@app.before_request
def init_session():
    g.my_session = Session()
    
    
@app.teardown_request
def remove_session(param):
    Session.remove()


if __name__ == '__main__':
    config = dict(
        debug = True,
        host = app.config['HOST'],
        port = app.config['PORT'],
    )
    app.run(**config)