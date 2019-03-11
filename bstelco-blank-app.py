#!/usr/bin/env python3
import bstelcoblankapp

if __name__ == '__main__':
	"""
	Sample blank application showing SIP data processing for VoLTE
	https://en.wikipedia.org/wiki/Session_Initiation_Protocol
	http://dilcis.eu/images/Specifications/SIP/General_SIP-Specification_v1.4.pdf
	
	1.) Modify TODOs in the ./etc/site.conf file
	2.) Run the application:
	./bstelco-blank-app.py -c ./etc/site.conf 	

	"""

	app = bstelcoblankapp.BSTelcoBlankApplication()
	app.run()
