from django.db import models
from django.forms import ModelForm
# Create your models here.

class Plumbing_Services (models.Model):
    Name = models.CharField(max_length=18)
    Contact = models.CharField(max_length=13)
    EMail = models.EmailField(max_length=40,blank=True)
    Password = models.CharField(max_length=10,default=0000)
    Status = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='site/plumbing/',blank=True)
    
    
    def __str__ (self):
        return self.Name
    class Meta :
        verbose_name_plural = 'Plumbing Services'   





class Tiling_Services (models.Model):
    Name = models.CharField(max_length=18)
    Contact = models.CharField(max_length=13)
    Email = models.EmailField(max_length=40,blank=True)
    Password = models.CharField(max_length=10,default=0000) 
    Status = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='site/tiling/',blank=True)
    
    
    
    def __str__ (self):
        return self.Name   
    class Meta :
        verbose_name_plural = 'Tiling services'  


class images_plumbing (models.Model):
    Name = models.ForeignKey(Plumbing_Services,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='site/plumbing')

class images_tiling (models.Model):
    Name=models.ForeignKey(Tiling_Services,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='site/tiling')              



