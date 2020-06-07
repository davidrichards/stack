from flask import Flask
from flask import request, jsonify
from stack.demo import version_1 as demo

server = Flask(__name__)

def run_request():
    data = request.json or {}
    a = data.get('a', 0)
    b = data.get('b', 0)
    params = [a, b]
    result = demo.predict(params)
    d = dict(
        classification=result[0],
        probabilities=result[1],
        data=data
    )
    return jsonify(d)
    
@server.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()

