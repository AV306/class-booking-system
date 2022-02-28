import datetime;
import json;


def retrieve( args ):
	"""Retrieve data from the sever."""
	# args is a multi_dict :(
	name = str(args.get('name', '')).lower(); # try to get the name of person
	number = 0;
	reason = str(args.get('reason', '')).lower();

	try:
		number = int(args.get('max', '')); # try to get the max number of data units (May throw exception)
	except ValueError:
		number = -1; # -1 tells it to do everything

	data = {"total": 0, "returned": 0, "data":[]};

	try:
		records = open( "records.nsj", "r" );
	except FileNotFoundError:
		# file not found, create it
		records = open( "records.nsj", "w" );
	else:
		for line in reversed(records.readlines()): # fill the dict ( We need to read it backwards :( )
				# O(n) complexity...
			
				data['total'] += 1;
		
				if data['returned'] == number:
					pass;
					
				else:
					try: 
						linedata = json.loads( line.strip() ); # parse data to dict
					except:
						pass;
					else:
						if name in linedata['name'].lower() and reason in linedata['reason'].lower():
							# check if the line is for the given person
							data['data'].append( linedata );
							data['returned'] += 1;

		records.close();
		return data;
			

						


def send( name, reason, details, password ):
	"""Send data to the server. TODO: Write to file start"""
	with open( "secrets.json", "r" ) as secrets:
		secret = json.load( secrets )['password'];
		
	if password == secret: # NOT SECURE TODO: Implement hashing
		with open( "records.nsj", "a" ) as records:
			records.write( json.dumps({"timestamp": str(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")), "name": name, "reason": reason, "details": details}) + "\n" );

		return True;

	else: return False;
