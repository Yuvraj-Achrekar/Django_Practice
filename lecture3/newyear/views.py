import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    date = datetime.datetime.now()
    return render(request,"newyear/index.html",{
        "newyear" : date.month == 1 and date.day == 1
    })