from django.shortcuts import render
from .models import Authentication, Notice

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
           
            return render(request, f"authentication/{roles}.html")
        
        else:
            return HttpResponse("Authentication Failed!")
    except:
        return HttpResponse("<h1>Internal Server Error!</h1>")
    
def publish(request):
    not_title = request.POST['notice_title']
    not_desc = request.POST['notice_desc']
    not_image = request.POST['filename2']
    try:
        add_notice = Notice(title=not_title,desc=not_desc, image=not_image)
        add_notice.save()
        return HttpResponse("Submitted!")
    except:
        return HttpResponse("Server is Busy")

    
