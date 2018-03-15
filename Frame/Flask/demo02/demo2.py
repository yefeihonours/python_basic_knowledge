from flask import Flask
from flask import request
from flask import make_response
from flask import abort

app = Flask(__name__)  # 创建Flask类的一个实例

@app.route("/login",methods=["GET"])
def login():
    html="<form method='post'>" \
    "<table>" \
    "<tr><td>请输入用户名</td><td><input type='text' name='username'/></td></tr>" \
    "<tr><td>请输入密码</td><td><input type='password' name='password'/></td></tr>" \
    "<tr><td><input type='submit' value='登录'/></td></tr>" \
    "</table>" \
    "</post>"
    return html

@app.route("/login",methods=["POST"])
def loginPost():
    username=request.form.get("username","")
    password=request.form.get("password","")
    if username=="test" and password=="123" :
        return "登录成功"+"<br><a href='http://localhost:5000/login'>返回</a>"
    else:
        return "登录失败"+"<br><a href='http://localhost:5000/login'>返回</a>"


@app.route("/res_test")
def res_test():
 response=make_response("<h1>hello world</h1")
 response.set_cookie("name","yefei")
 return response


@app.route("/req_test")
def req_test():
    val = ""
    for key, value in request.args.items():
        val += " %s = %s <br>" % (key, value)
    return val

@app.route("/")
def index():
    return "<h1>hello world</h1>",400

@app.route('/user/<name>')
def user(name):
    if name =='test':
        abort(500)
    return "<h1>hello %s!</h1>"%name


if __name__ == '__main__':  # Python入口程序
    app.run(debug=True)  # 使其运行于本地服务器上
