from flask import Flask, g
import app_config
from tools.orm import new_session, Session


app = Flask(__name__)
app.config['SECRET_KEY'] = app_config.secret_key


from routes.index import main as index_routes
from routes.weekly import main as weekly_routes


app.register_blueprint(index_routes)
app.register_blueprint(weekly_routes, url_prefix='/weekly')


@app.before_request
def init_session():
    g.my_session = Session()
    
    
@app.teardown_request
def remove_session(param):
    Session.remove()


if __name__ == '__main__':
    config = dict(
        debug = True,
        host = app_config.host,
        port = app_config.port,
    )
    app.run(**config)