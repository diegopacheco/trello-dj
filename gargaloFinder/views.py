from django.shortcuts import render_to_response
import json
import urllib2

def teste(request):
	boards = json.load(urllib2.urlopen("http://10.99.3.56:7070/api/v1/teams/boards"))
	bordJson = []
	for b in boards:
		board = json.load(urllib2.urlopen("http://10.99.3.56:7070/api/v1/teams/boards/"+b[ b.rindex('/')+1 ]));
		bordJson.append(board)
		for ee in board['queues'] :
			print(ee);
		


	return render_to_response('index.html', locals())
    

