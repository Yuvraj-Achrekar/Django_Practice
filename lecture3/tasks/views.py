from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class NewForm(forms.Form):
    task = forms.CharField(label="New task") 
    # priority = forms.IntegerField(label="priority",min_value=0,max_value=5)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        # print(request.POST["task"])
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return render(request,"tasks/add.html",{
        "form":NewForm()
    })
