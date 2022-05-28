from flask import Flask

app = Flask(__name__)

@app.route('/')
def one():
    return "API SUCCESS"

@app.route('/predict')
def predict():
    return "Predict API"

@app.route('/result')
def result():
    return "Result API"

@app.route('/app/data')
def data():
    return "App & Data API"

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000)