from django.db import models
from django.dispatch import Signal,receiver
from django.db.models.signals import post_save,pre_save
from django.db.models import F

from io import BytesIO
import logging
from PIL import Image
from django.core.files.base import ContentFile

# Create your models here.

cats = [
    ('Plumbing','Plumbing',),
    ('Tiles','Tiles',),
    ('Bathroom accessories','Bathroom accessories',),
]

class stock (models.Model):
    Item_Name = models.CharField(max_length=12)
    Quantity = models.PositiveIntegerField()
    Cost_price = models.PositiveIntegerField()
    Selling_price = models.PositiveIntegerField()
    date_added = models.DateTimeField(name='date added',auto_now_add=False)
    overall_price = models.PositiveIntegerField(null=True , blank=True)
    Category = models.CharField(max_length=35, blank=True,null=True,choices=cats)
    image = models.ImageField(upload_to='product-images',null=True,blank=True) 
    class Meta():
        verbose_name_plural='stock'
    def __str__(self):
        return self.Item_Name

    def save (self,*args,**kwargs):
        stock.objects.update(overall_price=F('Quantity')*F('Selling_price'))
        super(stock,self).save(*args,**kwargs)



"""THUMBNAIL_SIZE = (300, 300,)
logger = logging.getLogger(__name__)
@receiver(pre_save, sender=stock)
def generate_thumbnail(sender, instance, **kwargs):
    logger.info(
        "Generating thumbnail for product %d",
        instance.Item_Name,
    )
    image = Image.open(instance.image)
    image = image.convert("RGB")
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    temp_thumb = BytesIO()
    image.save(temp_thumb, "JPEG")
    temp_thumb.seek(0)  
    instance.thumbnail.save(
    instance.image.name,
    ContentFile(temp_thumb.read()),
    save=False,
    )
    temp_thumb.close()  """


@receiver(post_save,sender= stock)
def auto_calc (sender,instance,**kwargs):
    stock.objects.update(overall_price=F('Quantity')*F('Selling_price'))



        
    