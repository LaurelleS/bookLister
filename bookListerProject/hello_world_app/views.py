from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Laurelle Sekpe says \"Hello , world!\"")
# Create your views here.
