from flask import Flask,render_template

app = Flask(__name__)

#首页
@app.route('/')
def hello_world():
    return render_template('index.html')
#注册
@app.route('/register/')
def register():
    return render_template('register.html')

#登录
@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
