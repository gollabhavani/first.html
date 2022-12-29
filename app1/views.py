from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'bhavani','number':'12345'}
    return render(request,'first.html',context=d)
