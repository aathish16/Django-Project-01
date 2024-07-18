from django.shortcuts import render,redirect,HttpResponse

def home(request):
    return HttpResponse("<h1>view2</h1>")
def ak(request):
    return HttpResponse("<h2>hh</h2>")
def newfile1(request):
    return render(request,'new1.html')
def next1(request):
    return render(request,'next.html')
# Create your views here.
