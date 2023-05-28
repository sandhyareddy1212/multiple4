from django.shortcuts import render
from django.http import HttpResponse
def raaji(request):
    return HttpResponse('<b><center><marquee>mern programming language</center></marquee></b>')


def raaji(request):
    return render(request,'v.html')

# Create your views here.
