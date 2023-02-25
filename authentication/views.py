from django.shortcuts import render
from .models import Authentication

from django.http import HttpResponse

def index(request):


    return render(request,'authentication\login.html')

def main(request):
    name = request.POST['user']
    passw = request.POST['password']
    roles = request.POST['role']
    data = str(name + passw + roles)
    # return HttpResponse(data)
    try:
        password = str(Authentication.objects.get(userName=name, role=roles).password)
        if passw == password:
            return render(request, 'authentication/main.html')
        else:
            return HttpResponse("Authentication Failed!")
    except:
        return HttpResponse("<h1>Internal Server Error!</h1>")
    

    
