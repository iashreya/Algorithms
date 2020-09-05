from flask import Flask
from TSP import run

app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(run())
