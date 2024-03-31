from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("game/<str:game>",views.sample,name="game"),
]