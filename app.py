from flask import Flask
import app_config

app = Flask(__name__)
app.config['SECRET_KEY'] = app_config.secret_key


from routes.index import main as index_routes
from routes.weekly import main as weekly_routes


app.register_blueprint(index_routes)
app.register_blueprint(weekly_routes, url_prefix='/weekly')


if __name__ == '__main__':
    config = dict(
        debug = True,
        host = app_config.host,
        port = app_config.port,
    )
    app.run(**config)