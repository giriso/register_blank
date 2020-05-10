# -*- coding: utf-8 -*-
from flask import render_template, Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Гей'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
