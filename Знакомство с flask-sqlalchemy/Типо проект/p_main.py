# -*- coding: utf-8 -*-
from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/project.sqlite")
    crew = [['Scott', 'Ridley', 21, 'captain', "research engineer", "module_1", 'a@mail.ru', "cap"],
            ['Shreak', 'Bolotniy', 19, 'mechanic', 'fizik', 'module_1', 'sb@mail.ru', 'qwerty'],
            ['Anastasia', 'Reih', 16, 'pilot', 'fizik', 'module_2', 'ar@mail.ru', '1111'],
            ['Zoe', 'Blaskovitz', 22, 'cap_assistant', 'law enforcement', 'module_2', 'zb@mail.ru', 'thug']]
    session = db_session.create_session()
    for i in range(len(crew)):
        user = User()
        user.surname = crew[i][0]
        user.name = crew[i][1]
        user.age = crew[i][2]
        user.position = crew[i][3]
        user.speciality = crew[i][4]
        user.address = crew[i][5]
        user.email = crew[i][6]
        user.hashed_password = crew[i][7]
        session.add(user)
        session.commit()
    app.run(port=8084, host='127.0.0.2')


if __name__ == '__main__':
    main()
