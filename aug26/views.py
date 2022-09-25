from django.http import HttpResponse
from django.shortcuts import render
from car.models import service
from .forms import userform

def home(request):
    servicedata=service.objects.all()
    data={
        'servicedata':servicedata
    }
    return render(request,"index.html",data)
def about(request):
    return render(request,"about.html")
def booking(request):
    return render(request,"booking.html")
def form(request):
    ans=0
    num1=0
    num2=0
    data={}
    fn=userform
    try:
        if request.method =='POST':
            #n1=int(request.GET['num1'])
            #n2=int(request.GET['num2'])
            #n1=int(request.GET.get('num1'))
            #n2=int(request.GET.get('num2'))
            num1=int(request.POST['num1'])
            num2=int(request.POST['num2'])
            #print(n1+n2)
            ans=num1+num2
            data={
                'ans':ans,
                'num1':num1,
                'num2':num2,
                'form':fn
            }
            #url=('/about/?answer=ans'.formate.method(ans))
            #return HttpResponseRedirect('/about/')  
    except:
      pass    
    return render(request,"form.html",{'form':fn})