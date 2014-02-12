import requests

# Create your models here.

class example:
	def __init__(self, name, id, desc):
		self.name = name
		self.id = id
		self.desc = desc

class exampleDao:

	def find(self):
		r = requests.get('http://www.mocky.io/v2/52f0464f1990e56906990d8f')	
		js = r.json()
		return example(js[u'name'], js[u'id'], js[u'desc'])
			
class card:
	def __init__(self, name, id, points, startDate, endDate):
		self.name = name
		self.id = id
		self.points = points
		self.startDate = startDate
		self.endDate = endDate

class cardDao:

	def find(self):
		r = requests.get('http://10.99.2.82:7070/api/v1/teams/boards/1/queues/1/cards/1')	
		js = r.json()
		return card(js[u'name'], js[u'id'], js[u'points'], js[u'startDate'], js[u'endDate'])
			
