from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index , name ="AuthenticationPage"),
    # path('main/', views.main, name ="MainPage"),

]