#!/usr/bin/env python3
from bspumptelco import TelcoBaseApplication


class BSTelcoBlankApplication(TelcoBaseApplication):
	def __init__(self):
		"""
		SIP data processing for VoLTE
		https://en.wikipedia.org/wiki/Session_Initiation_Protocol
		http://dilcis.eu/images/Specifications/SIP/General_SIP-Specification_v1.4.pdf
		Input: File system
		Output: ElasticSearch
		"""

		super().__init__()

		# Register lookups required by pipelines

		self.add_mccmnc_lookup()
		self.add_uci_lookup()
		self.add_number2country_lookup()

		# Register connections

		self.add_es_connection()

		# Register pipelines

		# Compute ASR and SEER metrics
		# https://tools.ietf.org/html/rfc6076
		self.add_asrseer_pipeline()

		# Detection of anomalies
		self.add_alarm_sip_pipeline()

		self.add_sip_pipeline()


if __name__ == '__main__':
	"""
	Sample blank application showing SIP data processing for VoLTE
	https://en.wikipedia.org/wiki/Session_Initiation_Protocol
	http://dilcis.eu/images/Specifications/SIP/General_SIP-Specification_v1.4.pdf

	1.) Modify TODOs in the ./etc/site.conf file
	2.) Run the application:
	./bstelco-blank-app.py -c ./etc/site.conf 	

	"""

	app = BSTelcoBlankApplication()
	app.run()
