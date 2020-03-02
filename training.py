from flask import render_template, Flask


app = Flask(__name__)


@app.route('/training/<prof>')
def profe(prof):
    param = {}
    param['prof'] = prof
    return render_template('prof.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
