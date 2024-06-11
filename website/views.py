from django.shortcuts import render

def home(req):
    return render(req, 'website/templates/index.html')