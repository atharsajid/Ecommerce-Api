import numbers
from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    price=models.IntegerField()
    imagepath=models.CharField(max_length=250,blank=True)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.title