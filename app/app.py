from flask import Flask, request, redirect, url_for, flash, jsonify
import json, pickle
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/api/makecalc/', methods=['POST'])

def makecalc():
    """
    Function run at each API call
    No need to re-load the model
    """
    # reads the received json
    jsonfile = request.get_json()
    data = pd.read_json(json.dumps(jsonfile))
    print(data)

    res = dict()
    ypred = model.predict(data)
    for i in range(len(ypred)):
        res[i] = ypred[i]

    # returns a json file
    return jsonify(res)

if __name__ == '__main__':
    modelfile = 'modelfile.pkl'
    model = pickle.load(open(modelfile, 'rb'))
    app.run(host='0.0.0.0', debug=True, port=80)
