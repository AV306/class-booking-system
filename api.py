import json;
from flask import render_template;

def retrieve( args ):
	"""Retrieve data from the sever."""
	# args is a multi_dict :(
	query = args.get('query', ''); # try to get query type
	name = args.get('name', ''); # try to get the name of person
	number = args.get('max', ''); # try to get the max number of data units

	with open( "records.nsj", "r" ) as records:
		data = {"total": 0, "data": []};

		for line in records:
			data['total'] += 1;
			data['data'].append( json.loads(line) );

		return data;


def send( name, reason, details, password ):
	"""Send data to the server."""
	with open( "secrets.json", "r" ) as secrets:
		secret = json.load( secrets )['password'];
		
	if password == secret: # NOT SECURE TODO: Implement hashing
		with open( "records.nsj", "a" ) as records:
			records.write( json.dumps({"name": name, "reason": reason, "details": details}) + "\n" );

		return render_template( "index.html", auth=True );

	else: return render_template( "index.html", auth=False );