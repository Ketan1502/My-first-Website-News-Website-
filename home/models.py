from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(max_length=12)
    area=models.TextField()
    date=models.DateField()
   
    def __str__(self):
        return self.name

    