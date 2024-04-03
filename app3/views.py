from django.shortcuts import render

# Create your views here.
def conditionals(request):
    d={"a":100,"b":200,"c":3}
    return render(request,'conditionals.html',d)
def loop(request):
    d={'name':"ABCDEF"}
    return render(request,"loop.html",d)