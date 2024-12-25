from django.shortcuts import render
from django.http import HttpResponse  # Ensure this import is included

# Define the view
def my_blog(request):
    return HttpResponse("Hello, Blog!")
