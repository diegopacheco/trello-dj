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
			
