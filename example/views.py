# example/views.py


from django.http import HttpResponse templates

def index(request):
  
    return HttpResponse(request,"rush.html")
