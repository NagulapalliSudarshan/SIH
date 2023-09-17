from django.shortcuts import render,HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("hello world")

def landingPage(request):
    return render(request,"landingPage/landingPage.html",{"title":"LandingPage"})