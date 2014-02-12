from django.shortcuts import render_to_response
from models  import *

def hello(request):
	example = cardDao().find()
    	return render_to_response('templates/example.html', {'card' : card})

def burndown(request):
	burn = trelloDao().card()
        return render_to_response('templates/burndown.html', {'burn' : burn})