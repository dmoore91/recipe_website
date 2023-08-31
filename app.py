from flask import Flask, render_template  # import flask

from models import Schema

app = Flask(__name__)  # create an app instance


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":  # on running python app.py
    Schema()
    app.run()  # run the flask app
