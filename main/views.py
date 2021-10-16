from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
	context = {
			
            }
	
	return render(request, "main/index.html", context )


def contact(request):
	context = {
			
            }
	
	return render(request, "main/contact.html", context )


def about(request):
	context = {
			
            }
	
	return render(request, "main/about.html", context )