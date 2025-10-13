from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 
def password():

class student(models.Model):
    student_fristname=models.CharField(max_length=30, blank=False)
    student_lastname=models.CharField(max_length=30, blank=False)
    age= models.IntegerField
    email=models.EmailField(null=True)
    address=models.CharField(blank=True)
    phone_no=models.IntegerField()    
    password=models.CharField(blank=False)

    class Meta:
        from django.contrib.auth.models import User

        user = User.objects.get(username='existinguser')
        if user.check_password('correctpassword'):
            print("Password is correct!")
        else:
            print("Incorrect password.")