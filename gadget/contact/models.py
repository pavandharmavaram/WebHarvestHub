from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname=models.CharField( max_length=50)
    secondname=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    phone_number=models.CharField( max_length=50)
    message=models.TextField()
    
    def __str__(self):
        return self.firstname