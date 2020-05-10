from flask import Flask
from flask import url_for
import request

app = Flask(__name__)


@app.route('/')
def phrase1():
    return '<h1>Миссия Колонизация Марса</h1>'

@app.route('/u suck')
def sucker():
    return '<h1>Дарова Чувырла</h1>'


@app.route('/index')
def phrase2():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def advertisment():
    return '<p>Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>' \
           'Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!</p>'


@app.route('/image_mars')
def decoration():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/image.jpg')}">
                        <h2>Вот она какая, красная планета.</h2>
                      </body>
                    </html>'''


@app.route('/choice/<planet>')
def choice(planet):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet}</h1>
                        <div class="alert alert-light" role="alert">
                        Эта планета близка к Земле;
                        </div>
                        <div class="alert alert-success" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
<div class="alert alert-secondary" role="alert">
                      На ней есть вода и атмосфера;
                    </div>
<div class="alert alert-warning" role="alert">
                      На ней есть небольшое магнитное поле  
                    </div>
<div class="alert alert-danger" role="alert">
                      Наконец, она просто красива!
                    </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                            <title>Привет, результаты отбора</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <div class="alert alert-light" role="alert">
                            Претендента на участие в миссии {nickname}:
                            </div>
                            <div class="alert alert-success" role="alert">
                          Поздравляем! Ваш рейтинг после {level} этапа    отбора
                        </div>
    <div class="alert alert-secondary" role="alert">
                          составляет {rating}
                        </div>
    <div class="alert alert-warning" role="alert">
                          Желаем удачи!  
                          </body>
                        </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.2')
