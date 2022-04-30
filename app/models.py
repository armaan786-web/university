from tkinter import CASCADE
from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.ForeignKey(University,on_delete=models.CASCADE)
    registration_no = models.IntegerField()
    result = models.ImageField(upload_to = 'result')

    def __str__(self):
        return str(self.registration_no)
    
    
    
