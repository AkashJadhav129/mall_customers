
from flask import Flask,render_template,request
import numpy as np
import pickle

with open("model.pkl","rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl","rb") as scaler_file:
    scaler = pickle.load(scaler_file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cluster.html')

@app.route('/predict', methods = ['GET','POST'])
def predict():
    age = request.form['age']
    annual_income = request.form['annual_income']
    speding_score = request.form['spending_score']
    
    user_data = np.zeros(3)
    
    user_data[0] = age
    user_data[1] = annual_income
    user_data[2] = speding_score
    
    user_data_scale = scaler.transform([user_data])
    
    res = model.predict(user_data_scale)
    print(res)

    return render_template("display.html", data_user = res[0])

if __name__ == '__main__':
    app.run(debug=True)