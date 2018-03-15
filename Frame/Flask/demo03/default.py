from flask import render_template  # 头部，引入模板渲染方法
from flask import Flask

app = Flask(__name__)  # 创建Flask类的一个实例

@app.route("/login", methods=["GET"])
def login():
    return render_template("/login.html")
    # 渲染模板，默认找templates文件夹下的login.html文件

@app.route("/")
def index():
 return render_template("/index.html",site_name='myblog')

if __name__ == '__main__':  # Python入口程序
    app.run(debug=True)  # 使其运行于本地服务器上
