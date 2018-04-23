import datetime

errLogOut =  "Reports"

class Logger:
	"this class should eventually handle every error in the game, and shutdown the game if fatal error discovered"
	def __init__(self):
		"will log error files to Logs folder"
		self.report_list = []
		self.errLogOut = errLogOut

	def report(self, msg):
		"takes message and adds it to list of messages"
		self.report_list.append(msg + " " + )

	def format_report(self):
		"formats list as json"

	def save_report(self, filename, file):
		"saves formatted report at destination"		

	def log():
		"saves log file to errLogOut folder"
		dt = datetime.datetime
		filename = dt.year + "/" + dt.day + "/"+ dt.time
