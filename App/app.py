from flask import Flask

from urls import bp

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
