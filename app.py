from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import joblib
  

import flask

app = Flask(__name__)
clf = joblib.load('final_model.joblib')
scaler = joblib.load('standard_scaler.joblib')

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    to_predict_list = request.form.to_dict()
    user_input = (to_predict_list['user_input']).split(" ")
    user_input = [[float(inp) for inp in user_input]]
    user_input = scaler.transform(user_input)
    pred = clf.predict(user_input)
    if pred[0] == 0:
        prediction = "Setosa"

    elif pred[0] == 1:
        prediction = "Versicolor"
    else:
        prediction = "Virginica"    
    return flask.render_template('predict.html', prediction = prediction)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
