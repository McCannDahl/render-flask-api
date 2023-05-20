try:
    import secret # set env var
except:
    pass
import os
from flask import Flask, request, jsonify
from query import queryDocuments, queryExtractive, queryGenerative
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/documents', methods=['POST']) 
def documents():
    data = request.json
    input = data['input']
    data['output'] = queryDocuments(input)
    return jsonify(data)
@app.route('/extractive', methods=['POST']) 
def extractive():
    data = request.json
    input = data['input']
    data['output'] = queryExtractive(input)
    return jsonify(data)
@app.route('/generative', methods=['POST']) 
def generative():
    data = request.json
    input = data['input']
    data['output'] = queryGenerative(input)
    return jsonify(data)