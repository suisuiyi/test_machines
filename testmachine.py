#encoding: utf-8
from flask import Flask,render_template,request,redirect,url_for,session
import config
from exts import db
from models import User
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '用户已存在，请去登录页面登录'
        else:
            if password1 != password2:
                return '两次输入的密码不一致，请核对后再次输入'
            else:
                registerUser = User(telephone=telephone, username=username,password=password1)
                db.session.add(registerUser)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '该用户不存在，请注册后登录'
@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    if user:
        return {'user': user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
