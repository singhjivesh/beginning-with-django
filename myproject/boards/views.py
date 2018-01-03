from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')

 '''
views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')

Views are Python functions that receive an HttpRequest object and returns an HttpResponse object. Receive a request as a parameter and returns a response as a result. That’s the flow you have to keep in mind!

So, here we defined a simple view called home which simply returns a message saying Hello, World!.

Now we have to tell Django when to serve this view. It’s done inside the urls.py file:
'''
