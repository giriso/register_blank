from flask import render_template, Flask

app = Flask(__name__)


@app.route('/training/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('prof.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
