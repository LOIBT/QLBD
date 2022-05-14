from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField,StringField
from wtforms import validators
from wtforms.validators import DataRequired
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
class TestForm(FlaskForm):
    makh = IntegerField(label='Ma khach hang:', validators=[DataRequired()])
    tenkh = StringField(label='Ten khach hang:', validators=[DataRequired()])
    diachi = StringField(label='Dia chi:', validators=[DataRequired()])
    sdt = StringField(label='SDT:', validators=[DataRequired()])
    LoaiKH = StringField(label='Loai Khach Hang:', validators=[DataRequired()])
    
    # stringfield
    submit = SubmitField(label='Xac nhan')


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))
