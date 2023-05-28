from django.shortcuts import render
from django.http import HttpResponse
def neethu(request):
    return HttpResponse('<b><center><marquee>python programming language</marquee></center></b>')


def neethu(request):
    return render(request,'n.html')

# Create your views here.
