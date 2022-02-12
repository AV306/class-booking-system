import json;
from flask import render_template;

def handle( name, reason, details, password ):
	if password == "test": # NOT SECURE TODO: Implement hashing
		with open( "records.json", "w+" ) as records:
			# gets the json data from file and returns a dictionary
			try:
				data_dict = json.load( records ); 
			except:
				data_dict = {"data": []};
			finally:
				# append the new dict to the list under key "data" in the main dict
				data_dict['data'].append( {"name": name, "reason": reason, "details": details} );

				records.seek(0); # idk what this does it just works

	# put everything back
			json.dump( data_dict, records, indent=4 ); 

		return render_template( 'index.html', auth=True );

	else:
		return render_template( 'index.html', auth=False );
