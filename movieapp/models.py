from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    des = models.TextField(blank=True, null=True)
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

def __str__(self):
    return self.name
