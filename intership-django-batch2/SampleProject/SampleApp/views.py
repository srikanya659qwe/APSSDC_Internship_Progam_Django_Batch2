from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Hello guys welcome to django internship</h1>")


def sam(request):
	return HttpResponse("<h2 style=color:green;background-color:yellow;font-size:45px><center>Django Internship</center></h2>")

def dynamic(request,id):
	return HttpResponse("<h2><center>My Rollnumber is:{}</center></h2>".format(id))

def data(request,name):
	return HttpResponse("<h1 style=color:navy;background-color:green;font-style:italic><center>My Name is :{}</center></h1>".format(name))