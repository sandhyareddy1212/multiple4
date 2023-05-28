from django.urls import path
from nithya.views import *
app_name='brundha'
urlpatterns=[
    path('neethu/',neethu,name='neethu'),
]