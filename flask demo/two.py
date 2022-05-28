from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('two.html')


@app.route('/result')
def result():
    return render_template('three.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5500, debug = True)