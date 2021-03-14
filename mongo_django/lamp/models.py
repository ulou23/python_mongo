from django.db import models
import datetime

class Category(models.Model):
    title = models.CharField(max_length=20)


    objects = models.Manager()

    def __str__(self):
        return self.title

class Lamp(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    phone=models.IntegerField(null=True)
    person=models.CharField(max_length=50, default='myBoss')

    categories=models.ManyToManyField(Category)



    def __str__(self):
        return self.name

    objects=models.Manager()





# Create your models here.
