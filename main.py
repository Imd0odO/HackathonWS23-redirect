from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def identify():
    return 'Poker Python Player'


@app.route('/', methods=['POST'])
def bet():
    return requests.post("http://home.anxietyprime.de:8000", json=request.json).json()
