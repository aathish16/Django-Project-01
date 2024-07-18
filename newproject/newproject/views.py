from django.shortcuts import render,redirect,HttpResponse

def home(request):
    return HttpResponse("<h1>view</h1>")
def ak(request):
    return HttpResponse("<h2>hh</h2>")
def newfile1(request):
    return render(request,'new1.css')
