from django.shortcuts import render

# Create your views here.
def second(request):
    d={'name':'bhavi','numbe':'7258'}
    return render(request,'second.html',context=d)
