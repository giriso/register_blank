# -*- coding: utf-8 -*-
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from flask import Flask, render_template, abort, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Навыки', validators=[DataRequired()])
    address = StringField('Блок проживания', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')


class LoginForm(FlaskForm):
    email = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


def main():
    db_session.global_init("db/project.sqlite")
    app.run(port=8084, host='127.0.0.2')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('submit')
        if form.password.data != form.password_again.data:
            print(-1)
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            email=form.email.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login')
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        print(user and user.check_password(form.password.data))
        print(user.check_password(form.password.data))
        print(user)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        print(form.password.data, user.hashed_password)
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    print(form.validate_on_submit())
    return render_template('login.html', title='Авторизация', form=form)



if __name__ == '__main__':
    main()
