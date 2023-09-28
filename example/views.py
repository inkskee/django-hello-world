# example/views.py


from django.http import HttpResponse, render

def index(request):
  
    return render(request,"rush.html")
