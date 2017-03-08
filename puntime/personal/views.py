from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content': ['Please email me if you have any questions.' ,'At admin@jamuura.com']})
