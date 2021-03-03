from django.db import models
import datetime

class Category(models.Model):
    title = models.CharField(max_length=100)

    objects = models.Manager()

class Lamp(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    phone=models.IntegerField(null=True)

    category=models.ManyToManyField(Category,verbose_name="list of lamps")

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name

    objects=models.Manager()





# Create your models here.
