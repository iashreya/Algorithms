from flask import Flask, render_template, url_for, request
from TSP import run

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world(n=5):
		
		print("Value of n: ",n)
		res = run(n)
		path = str(res["path"])
		time_taken = str(res["time_taken"])
		path_length = str(res["path_length"])
		return render_template('main_page.html', path=path, time_taken=time_taken, path_length=path_length)
