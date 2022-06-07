from flask import Flask
from key import config
import cx_Oracle

pool = cx_Oracle.SessionPool(user=config['oracle_user'], password=config['oracle_passwd'], dsn=config['DSN'], min=3, max=3, increment=0, getmode=cx_Oracle.SPOOL_ATTRVAL_WAIT, encoding="UTF-8")

app = Flask(__name__)
app.config['SECRET_KEY'] = config['skey']

dsphieu = []
phieu = {
    'madonhang': '',
    'mavandon': '',
    'tennguoigui': '',
    'sdtgui': '',
    'dcgui': '',
    'tennguoinhan': '',
    'sdtnhan': '',
    'dcnhan': '',
    'mota': '',
    'thoigiandat': ''
}

from app import routes


# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     def __repr__(self):
#         return f'<User: {self.username}>'

# users = []
# users.append(User(id=1, username='Anthony', password='password'))
# users.append(User(id=2, username='Becca', password='secret'))
# users.append(User(id=3, username='Carlos', password='somethingsimple'))
