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
			
class trelloDao:

	def card(self):
		r = requests.get('http://10.99.3.56:7070/api/v1/teams/boards/1/queues/1/cards/1')
		js = r.json()
		return card(js[u'name'], js[u'id'], js[u'points'], js[u'startDate'], js[u'endDate'],js[u'leadTime'][u'codeReview'])			

class card:
	def __init__(self, name, id, points, startDate, endDate, codeReview):
		self.name = name
		self.id = id
		self.points = points
		self.startDate = startDate
		self.endDate = endDate
		self.codeReview = codeReview

class cardDao:

	def find(self):
		r = requests.get('http://10.99.3.56:7070/api/v1/teams/boards/1/queues/1/cards/1')	
		js = r.json()
		return card(js[u'name'], js[u'id'], js[u'points'], js[u'startDate'], js[u'endDate'])	

class queue:
	def __init__(self, id, name, cards):
		self.id = id
		self.name = name
		self.cards = cards
	
				
class queueDao:
	def findByrange(self,startDate,endDate):	
		
		r = requests.get('http://10.99.2.153:7070/api/v1/teams/boards/1/queues/1?from=' + startDate+'&to=' + endDate)	
		js = r.json()
		return queue(js[u'id'], js[u'name'], js[u'cards'])   	