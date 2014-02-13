from django.shortcuts import render_to_response
import json
import urllib2

def teste(request):
	boards = json.load(urllib2.urlopen("http://10.99.3.56:7070/api/v1/teams/boards"))
	bordJson = []
	for b in boards:
		board = json.load(urllib2.urlopen(b.replace('localhost','10.99.3.56')))
		bordJson.append(board)
		for ee in board['queues'] :
			cards = json.load(urllib2.urlopen(ee.replace('localhost','10.99.3.56')))
			for c in cards['cards']:
				card = json.load(urllib2.urlopen(c.replace('localhost','10.99.3.56')))
				codeReview = card['leadTime']['codeReview']
				if int(codeReview) == 0 and card['endDate'] != '':
					print('Nao teve codeReview')


			


	return render_to_response('index.html', locals())
    

