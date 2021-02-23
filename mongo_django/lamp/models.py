from djongo import models


class Category(models.Model):
    title = models.CharField(max_length=20)

class Lamp(models.Model):
    created=models.DateTimeField(auto_now_add=True,auto_now=False)
    name=models.CharField(max_length=20)
    phone=models.IntegerField(null=True)
    contact_person=models.CharField(max_length=40)
    category=models.ArrayReferenceField(
        to=Category,
        on_delete=models.CASCADE,
    )



# Create your models here.
