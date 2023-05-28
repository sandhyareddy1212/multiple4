from django.urls import path
from swathi.views import *
app_name='haripriya'
urlpatterns=[
    path('malnad/',malnad,name='malnad'),
]