from django.urls import path
from vani.views import *
app_name='bavya'
urlpatterns=[
    path('raaji/',raaji,name='raaji'),
]