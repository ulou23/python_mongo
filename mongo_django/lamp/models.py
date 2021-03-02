from django.db import models
import datetime

class Category(models.Model):
    title = models.CharField(max_length=20)

class Lamp(models.Model):
    published = models.DateTimeField(default=datetime.datetime.now)
    name=models.CharField(max_length=20)
    phone=models.IntegerField(null=True)

    category=models.ManyToManyField(Category,on_delete=models.CASCADE, verbose_name="list of lamps")

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name





# Create your models here.
