from app import app, pool 
from flask import render_template
from app.forms import TestForm
from app.forms import User
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

@app.route('/')
@app.route('/home')
def index():
    return render_template('base.html')

@app.route('/get')
def get():
    connection = pool.acquire()
    cursor = connection.cursor();
    cursor.execute("select * from KHACHHANG_T")
    r = cursor.fetchall()
    pool.release(connection)
    return str(r)


@app.route('/login1', methods=['GET', 'POST'])
def login1():
    form2 = TestForm()
    if form2.validate_on_submit():
        makh = form2.makh.data
        tenkh = form2.tenkh.data
        diachi = form2.diachi.data
        sdt = form2.sdt.data
        LoaiKH = form2.LoaiKH.data
        connection = pool.acquire()
        cursor = connection.cursor();
        query = f"insert into KHACHHANG_T values ({makh},'{tenkh}','{diachi}','{sdt}','{LoaiKH}')"
        cursor.execute(query)
        connection.commit();
        pool.release(connection)
    return render_template('login1.html', form=form2)








# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     def __repr__(self):
#         return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))




@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')
# @app.before_request
# def before_request():
#     g.user = None

#     if 'user_id' in session:
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user
        

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session.pop('user_id', None)

#         username = request.form['username']
#         password = request.form['password']
        
#         user = [x for x in users if x.username == username][0]
#         if user and user.password == password:
#             session['user_id'] = user.id
#             return redirect(url_for('profile'))

#         return redirect(url_for('login'))

#     return render_template('login.html')

# @app.route('/profile')
# def profile():  
#     if not g.user:
#         return redirect(url_for('login'))

#     return ('profile.html')






# #themvao
# from flask import (
#     Flask,
#     g,
#     redirect,
#     render_template,
#     request,
#     session,
#     url_for
# )
# #end them
# #them vao

# # @app.route('/login', methods=['GET', 'POST'])

# # class User:
# #     def __init__(self, id, username, password):
# #         self.id = id
# #         self.username = username
# #         self.password = password

# #     def __repr__(self):
# #         return f'<User: {self.username}>'

# users = []
# users.append(User(id=1, username='Anthony', password='password'))
# users.append(User(id=2, username='Becca', password='secret'))
# users.append(User(id=3, username='Carlos', password='somethingsimple'))


# app = Flask(__name__)
# app.secret_key = 'somesecretkeythatonlyishouldknow'

# @app.before_request
# def before_request():
#     g.user = None

#     if 'user_id' in session:
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user
        

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session.pop('user_id', None)

#         username = request.form['username']
#         password = request.form['password']
        
#         user = [x for x in users if x.username == username][0]
#         if user and user.password == password:
#             session['user_id'] = user.id
#             return redirect(url_for('profile'))

#         return redirect(url_for('login'))

#     return render_template('login.html')

# @app.route('/profile')
# def profile():
#     if not g.user:
#         return redirect(url_for('login'))

#     return render_template('profile.html')
        
# #end them vao 

