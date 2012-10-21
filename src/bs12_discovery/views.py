from django.shortcuts import render

def index(request):
    return render(request, "bs12_discovery/index.html")
