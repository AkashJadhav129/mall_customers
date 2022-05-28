from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Index API"

@app.route("/fail/<int:score>")
def fail(score):
    return "The person is failed and mark is = "+str(score)

@app.route("/success/<int:score>")
def success(score):
    return "The person is passed and mark is = "+str(score)


@app.route("/user/<int:mark>")
def result_check(mark):
    if mark >= 35:
        result = 'success'
    else:
        result = 'fail'
    return redirect(url_for(result, score=mark))

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug =True)