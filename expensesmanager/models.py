from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Income(models.Model):
    title = models.CharField(max_length=200)
    amount  = models.PositiveIntegerField()
    date =models.DateField(auto_now=True)
    image = models.ImageField(upload_to='income/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Expenses(models.Model):
    title = models.CharField(max_length=200)
    amount  = models.PositiveIntegerField()
    date =models.DateField(auto_now=True)
    image = models.ImageField(upload_to='income/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title