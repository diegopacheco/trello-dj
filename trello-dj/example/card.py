import requests

# Create your models here.

class card:
	def __init__(self, name, id, points, startDate, endDate):
		self.name = name
		self.id = id
		self.points = points
		self.startDate = startDate
		self.endDate = endDate

class cardDao:

	def find(self):
		r = requests.get('http://localhost:7070/api/v1/teams/boards/1/queues/1/cards/1')	
		js = r.json()
		return example(js[u'name'], js[u'id'], js[u'points'], js[u'startDate'], js[u'endDate'])
			
