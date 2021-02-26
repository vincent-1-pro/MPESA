from django.db import models

# Create your models here.

class Players(models.Model):
    name=models.CharField(max_length=30)
    img= models.ImageField(upload_to='pictures')
    desc=models.TextField()
    price= models.IntegerField()
    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)

   # id: int
    #name: str
    #img: str
    #desc: str
    #price: int
    #date: int
class Players2(models.Model):
    
    name=models.CharField(max_length= 30)
    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    describe=models.TextField()
