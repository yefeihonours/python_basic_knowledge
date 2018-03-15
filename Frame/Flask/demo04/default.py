from flask.ext.bootstrap import Bootstrap
from flask import request
from flask import render_template  # 头部，引入模板渲染方法
from flask import Flask
from flask import session


app = Flask(__name__)  # 创建Flask类的一个实例
bootstrap = Bootstrap(app)

@app.route("/login", methods=["GET"])
def login():
    return render_template("/login.html")

    # 渲染模板，默认找templates文件夹下的login.html文件

@app.route("/login",methods=["POST"])
def loginPost():
    username=request.form.get("username","")
    password=request.form.get("password","")
    print('------输入信息-------',username,password)
    if username=="test" and password=="123" :
        print('test用户登录成功')
        session["user"]=username
        return render_template("/index.html",name=username,site_name='myblog')
    else:
        return "登录失败"



if __name__ == '__main__':  # Python入口程序
    app.secret_key = 'super secret key'
    app.run(debug=True)  # 使其运行于本地服务器上

