from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


from routes.index import main as index_routes

app.register_blueprint(index_routes)


if __name__ == '__main__':
    config = dict(
        debug = True,
        host = '0.0.0.0',
        port = 3000,
    )
    app.run(**config)