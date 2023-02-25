from django.db import models

# Create your models here.

class Authentication(models.Model):
    person_id = models.AutoField
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.userName
