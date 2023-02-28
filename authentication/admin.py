from django.contrib import admin
from .models import Authentication , Notice, Teacher


# Register your models here.

admin.site.register(Authentication)
admin.site.register(Notice)
admin.site.register(Teacher)