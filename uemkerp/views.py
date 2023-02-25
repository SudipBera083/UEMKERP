from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def main(request):
#     name = request.POST['user']
#     passw = request.POST['password']
#     roles = request.POST['role']
#     print(name + passw + roles)
    