from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def say_welcome():
    '''return "welcome"'''

    html = '<h1>welcome</h1>'
    return html


@app.route('/welcome/home')
def say_welcome_home():
    '''return "welcome home"'''
    html = '<h1>welcome home</h1>'
    return html

@app.route('/welcome/back')
def say_welcome_back():
    '''return "welcome back"'''
    html = '<h1>welcome back</h1>'
    return html