from flask import Flask, request, redirect, url_for, flash, jsonify
import json, pickle
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Function run at each API call
    """

    # Read model from disk
    modelfile = 'modelfile.pkl'
    model = joblib.load(modelfile)

    # reads the received json
    jsonfile = request.get_json()
    df = pd.read_json(json.dumps(jsonfile),orient='index')
    df = np.array(df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']])

    # Predicts
    ypred = model.predict(df).tolist()

    # Creates dictionary of predictions
    result = dict()
    for i in range(len(ypred)):
        result[i] = ypred[i]

    # returns a json file
    #return pd.DataFrame.to_json(df)
    #return jsonify(ypred)
    return json.dumps(result)


@app.route('/api/details', methods=['GET'])
def details():
    try:
        lr = joblib.load("./modelfile.pkl")
        training_set = joblib.load("./training_data.pkl")
        labels = joblib.load("./training_labels.pkl")

        return jsonify({"score": lr.score(training_set, labels), "coefficients": lr.coef_.tolist(), "intercepts": lr.intercept_.tolist()})
    except (ValueError, TypeError) as e:
        return jsonify("Error when getting details - {}".format(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
