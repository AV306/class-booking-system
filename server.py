from flask import Flask;
from flask import request;
from flask import render_template;
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
		return render_template( "index.html", auth=api.send( name, reason, details, password ) );


@app.route('/api', methods=['GET'])
def onApiGet():
	"""Handle GET requests to the data route."""
	return api.retrieve( request.args );


@app.route('/data', methods=['GET'])
def onDataGet():
	"""Return a human-readable version of the api data."""
	# retrieve the api data.
	data = api.retrieve( request.args );

	# format the data into a human-readable format.

	return render_template( "data_table.html", data=data );


@app.errorhandler(404)
def notFound( error ):
	return render_template( "errors/error.html", error=error ), 404

@app.errorhandler(500)
def serverError( error ):
	return render_template( "errors/error.html", error=error ), 500