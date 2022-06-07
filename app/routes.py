from app import app, pool, dsphieu, phieu
from flask import render_template
from app.forms import TestForm, DangKyDonForm, SearchForm
from app.forms import User
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    flash
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


@app.route('/dangkydonhang', methods=['GET', 'POST'])
def dkdh():
    form2 = DangKyDonForm()
    if form2.validate_on_submit():
        cccd = form2.cccd.data
        tenkh = form2.tenkh.data
        dc_kh = form2.dc_kh.data
        sdt = form2.sdt.data
        dc_gui = form2.dc_gui.data
        dc_nhan = form2.dc_nhan.data
        ghichu = form2.ghichu.data
        mota = form2.mota.data
        dai = form2.dai.data
        rong = form2.rong.data
        cao = form2.cao.data
        kl = form2.kl.data
        ml = form2.ml.data
        cod = form2.cod.data
        tennn = form2.tennn.data
        sdt_nn = form2.sdt_nn.data
        connection = pool.acquire()
        cursor = connection.cursor();
        query = """call dangky_donhang(:cccd,:tenkh,:dc_kh,:sdt,:dc_gui,:dc_nhan,:ghichu,:mota,:dai,:rong,:cao,:kl,:ml,:cod,:tennn,:sdt_nn,:manv)"""
        if cccd == "":
            query = """call dangky_donhang(null,:tenkh,:dc_kh,:sdt,:dc_gui,:dc_nhan,:ghichu,:mota,:dai,:rong,:cao,:kl,:ml,:cod,:tennn,:sdt_nn,:manv)"""
            cursor.execute(query, [tenkh, dc_kh, sdt, dc_gui, dc_nhan,ghichu, mota,dai,rong,cao,kl,ml,cod,tennn,sdt_nn, 1])
        else:
            cursor.execute(query, [cccd, tenkh, dc_kh, sdt, dc_gui, dc_nhan,ghichu, mota,dai,rong,cao,kl,ml,cod,tennn,sdt_nn, 1])
        connection.commit()
        pool.release(connection)
        flash('Dang ky don hang thanh cong')
        return redirect(url_for('dkdh'))
    return render_template('dangkydonhang.html', form=form2)

    @app.route('/tracuu', methods=['GET', 'POST'])
def tracuu():
    form2 = SearchForm();
    if form2.validate_on_submit():
        mvd = form2.mavandon.data
        if len(dsphieu) != 0:
            dsphieu.pop(0)
        connection = pool.acquire()
        cursor = connection.cursor();
        query = """select p.madonhang, p.mavandon, p.tennguoinhan, p.sdtnhan, d.thoigiandat, d.diachigui, d.diachinhan, d.motasp, k.tenkhachhang, k.sdt
    from phieudonhang p inner join donhangdk d
    on p.madk = d.madk inner join khachhang k
    on d.makhachhang = k.makhachhang
    where mavandon = :mavandon"""
        cursor.execute(query,[mvd])
        r = cursor.fetchone()
        phieu['madonhang'] = r[0]
        phieu['mavandon'] = r[1]
        phieu['tennguoigui'] = r[8]
        phieu['sdtgui'] = r[9]
        phieu['dcgui'] = r[5]
        phieu['tennguoinhan'] = r[2]
        phieu['sdtnhan'] = r[3]
        phieu['dcnhan'] = r[6]
        phieu['mota'] = r[7]
        phieu['thoigiandat'] = r[4]
        dsphieu.append(phieu)
        pool.release(connection)
        return redirect(url_for('tracuu'))
    return render_template('tracuu.html', form=form2, dsphieu=dsphieu)







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

