from flask import Flask;
from flask import request;
from flask import render_template;
import json;
import api;

app = Flask(__name__);

@app.route('/', methods = ['GET', 'POST'])
def onIndexGetOrPost():
	"""Handle HTTP requests to the main route."""
	if request.method == 'GET':
		# send the submit page
		return render_template( 'index.html' );
		
	elif request.method == 'POST':
		# form data
		name = request.form["name_input"];
		reason = request.form["reason_input"];
		details = request.form["details_input"];
		password = request.form["password_input"];
		return api.send( name, reason, details, password );


@app.route('/data', methods=['GET'])
def onDataGet():
	"""Handle GET requests to the data route."""
	return api.retrieve( request.args );