from django.db import models
import random
import string
# Create your models here.

class Authentication(models.Model):
    person_id = models.AutoField
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.userName

class Notice(models.Model):
    date = models.DateField(auto_now_add= True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to = "notice/images", default="")

    def __str__(self):
        return self.title

class Teacher(models.Model):
    def get_random_string(length):
    # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return f"{result_str}{random.randint(5, 100)}"

    teacher_id  = models.AutoField
    teacher_name = models.CharField(max_length=50)
    teacher_father = models.CharField(max_length=50)
    teacher_motheer = models.CharField(max_length=50)
    teacher_degree = models.CharField(max_length=50)
    teacher_university = models.CharField(max_length=50)
    teacher_passingYear = models.IntegerField()   
    teacher_dob = models.DateField()
    teacher_department = models.CharField(max_length=50)
    teacher_post = models.CharField(max_length=50)
    teacher_image = models.ImageField(upload_to="teacher/images")
    teacher_userName = models.CharField(max_length=10 , default=get_random_string(5))

    teacher_password = models.CharField(max_length=15, default=get_random_string(10))

    
    def __str__(self):
           return self.teacher_name
