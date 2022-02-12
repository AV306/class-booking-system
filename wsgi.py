from flask import Flask;
from flask import request;
from flask import Response;
from flask import render_template;
import json;
import core;

app = Flask(__name__);

@app.route("/", methods = ['GET', 'POST'])
def onIndexGetOrPost():
	if request.method == 'GET':
		# send the submit page
		return render_template( 'index.html' );
		
	elif request.method == 'POST':
		# form data
		name = request.form["name_input"];
		reason = request.form["reason_input"];
		details = request.form["details_input"];
		password = request.form["password_input"];
		return core.handle( name, reason, details, password );


@app.route("/data", methods=['GET'])
def onDataGet():
	with open( "records.json", "r" ) as records:
		return json.load( records );