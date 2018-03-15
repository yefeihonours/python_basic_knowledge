from flask import Flask, render_template, session, g, current_app
import time

app = Flask(__name__)
@app.route('/')
def index():
    session['user'] = 'guest'
    g.db = 'mysql'
    return render_template('hello.html',name = '<em>World</em>')

@app.context_processor
def appinfo():
    return dict(appname=current_app.name)

@app.context_processor
def get_current_time():
    def get_time(timeFormat="%b %d, %Y - %H:%M:%S"):
        return time.strftime(timeFormat)
    return dict(current_time=get_time)

app.secret_key = '123456'

if __name__ == '__main__':
    app.run(debug=True)