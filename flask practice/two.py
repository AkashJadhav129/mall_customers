import re
from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def one():
    return render_template('index.html')


@app.route('/admin/<int:name>')
def two(name):
    return "My name is " + str(name)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)