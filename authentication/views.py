from django.shortcuts import render
from .models import Authentication, Notice

from django.http import HttpResponse

from .forms import NoticeForm
from math import ceil

def index(request):


    return render(request,'authentication\login.html')

def main(request):
    
        
    form = NoticeForm()
    notices=  Notice.objects.all()
    n = len(notices)
    nSlides = n//4 + ceil((n/4) - (n//4))

    parms = {'no_of_slides':nSlides, 'range':range(1,nSlides), 'data': notices,'forms':form, 'f_title':"notices[0].title", "f_desc": notices[0].desc }

    name = request.POST['user']
    passw = request.POST['password']
    roles = request.POST['role']
    try:
        password = str(Authentication.objects.get(userName=name, role=roles).password)
        if passw == password:
            print("successfull")
           
            return render(request, f"authentication/{roles}.html",parms)
        
        else:
            print("fail")
            return HttpResponse("Authentication Failed!")
    except:
        return HttpResponse("<h1>Internal Server Error!</h1>")
    
def publish(request):
    if request.method == "POST":
        try:
            form = NoticeForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()
            return HttpResponse("Done")
        except Exception(e):
            return HttpResponse("e")
    
def ShowNotice(request):
    pass



    
