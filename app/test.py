import requests
import json

url = 'http://127.0.0.1:80/api/predict'

text = json.dumps({"0": {"sepal length (cm)": 4.9, "sepal width (cm)": 3., "petal length (cm)": 1.4, "petal width (cm)": 0.2},
                    "1": {"sepal length (cm)": 7.0, "sepal width (cm)": 3.2, "petal length (cm)": 4.7, "petal width (cm)": 1.4},
                    "2": {"sepal length (cm)": 5.9, "sepal width (cm)": 3.0, "petal length (cm)": 5.1, "petal width (cm)": 1.8}})

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=text, headers=headers)
print(r, r.text)


singletext = json.dumps({"0": {"sepal length (cm)": 4.9, "sepal width (cm)": 3., "petal length (cm)": 1.4, "petal width (cm)": 0.2}})

r2 = requests.post(url, data=singletext, headers=headers)
print(r2, r2.text)
