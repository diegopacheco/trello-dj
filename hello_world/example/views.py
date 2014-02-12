from django.shortcuts import render_to_response
from models  import *

def hello(request):
	example = exampleDao().find()
        return render_to_response('templates/example.html', {'example' : example})
