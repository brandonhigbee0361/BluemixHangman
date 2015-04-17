from websocket import create_connection

class PolyBlueClient(object):

	def __init__(self, app_name):
		self.client = create_connection('ws://' + app_name + '.mybluemix.net/socket?Id=2')
	
	def sendOutput(self, message):
		self.client.send(message)

	def getInput(self, message):
		self.sendOutput(message)
		result = None
		while result is None:
			result = self.client.recv()
		return result

	def close(self):
		self.client.close()
