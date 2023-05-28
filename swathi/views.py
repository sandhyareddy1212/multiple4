from django.shortcuts import render
from django.http import HttpResponse
def malnad(request):
    return HttpResponse('<b><center><marquee>java programming language</center></marquee></b>')



def malnad(request):
    return render(request,'s.html')

# Create your views here.
