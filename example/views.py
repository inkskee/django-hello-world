# example/views.py


from django.http import HttpResponse

def index(request):
  
    return HttpResponse(request,"rush.html")
