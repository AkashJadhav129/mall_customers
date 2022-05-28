
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods = ['GET','POST'])
def data():
    if request.method == "POST":
        user_data = request.form
        print(user_data)

    return render_template("display.html", data_user = user_data)

if __name__ == '__main__':
    app.run(debug=True)