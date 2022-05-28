from flask import Flask, redirect, url_for
from pydantic import UrlHostTldError
from sympy import re

app = Flask(__name__)

@app.route("/admin/<fname>")
def admin(fname):
    return "Welcome Admin "+ fname


@app.route("/guest/<fname>")
def guest(fname):
    return "Welcome Guest " + fname

@app.route("/user/<user_name>")
def user(user_name):
    if user_name == 'Akash':
        result = 'admin'
    else:
        result = 'guest'
    
    return redirect(url_for(result,fname=user_name))

if __name__ == '__main__':
    app.run(debug=True)