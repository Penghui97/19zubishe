
from flask import Flask, render_template, request, redirect, url_for, session, flash

# from From import MyForm

app = Flask(__name__, template_folder='Templates')

app.config['SECRET_KEY'] = 'project'
app.secret_key = 'project'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = MyForm()
    # if form.validate_on_submit():  # 将会检查是否是一个 POST 请求并且请求是否有效。
    #     return redirect(url_for(''))  # 如有有效就重定向到首页
    # name = request.form.get('name')
    # password = request.form.get('password')
    # print(name)
    # return render_template('rendering.html', form=form)
    name = request.form.get('username')
    password = request.form.get('password')
    if name == 'admin' and password == '123':
        session['name'] = name
        return redirect(url_for('login'))
    if name != 'admin':
        flash('no this name')
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
