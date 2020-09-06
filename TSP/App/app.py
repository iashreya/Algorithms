from flask import Flask, render_template, url_for
from TSP import run

app = Flask(__name__)

@app.route('/')
def hello_world():
    res = run()
    path = str(res["path"])
    time_taken = str(res["time_taken"])
    path_length = str(res["path_length"])
    return render_template('main_page.html', path=path, time_taken=time_taken, path_length=path_length)
