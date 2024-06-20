from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<h1><marquee>Srujana Tinnavara,Era Vadilastunnavaaaa......<marquee></h1>')

def meghana(request):
    return HttpResponse('<h1><marquee>My Name is Meghanaaa Sir......<marquee></h1>')


def harshad(request):
    return HttpResponse('<h1><marquee>My Name is Harshad Sir......<marquee></h1>')
