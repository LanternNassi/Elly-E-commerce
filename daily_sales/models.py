from django.db import models
import django.dispatch 
from django.dispatch import receiver
from django.db.models.signals import post_init,pre_init,pre_save,post_save
from django.db.models import F
from stock.models import stock
import json


# Create your models here
# 
# .




class daily_sales (models.Model):
    Day = models.CharField(max_length=10)
    Date_sold = models.DateTimeField(auto_now_add=False )
    Total_sales = models.IntegerField(null=True,blank = True)
    class Meta():
        verbose_name_plural='daily sales'
    def __str__(self):
        return self.Day


class product_entry (models.Model):
    Day = models.ForeignKey(daily_sales,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(stock,related_name='Day_items',on_delete=models.CASCADE)
    Quantity = models.IntegerField(null = True,blank = True)    
    Selling_price = models.IntegerField(null = True,blank = True)
    Total_price = models.IntegerField(null = True,blank = True)
    def save (self,*args,**kwargs):
        product_entry.objects.update(Total_price=F('Quantity')*F('Selling_price'))
        e = stock.objects.filter(Item_Name=self.product)
        for b in e :
            inert_quantity = b.Quantity - self.Quantity
            stock.objects.filter(Item_Name=self.product).update(Quantity=inert_quantity)
            stock.objects.update(overall_price=F('Quantity')*F('Selling_price'))
        super(product_entry,self).save(*args,**kwargs)
        
        inintial_value = 0
        w = product_entry.objects.filter(Day=self.Day)
        for p in w : 
            inintial_value += p.Total_price
        daily_sales.objects.filter(Day = self.Day).update(Total_sales=inintial_value)
        super(product_entry,self).save(*args,**kwargs)
        stock.objects.update(overall_price=F('Quantity')*F('Selling_price'))
        
        
               
        
       
                
                
                
                
        #for pe in w :
        

   # def __init__ (self,*args,**kwargs):
    #    try:
     #       stock.objects.get(Item_Name=self.product).update(Quantity=F('Quantity')-F('self.Quantity'))
      #      super(product_entry,self).__init__(*args,**kwargs)
       # except:
        #    pass     
              
        


    def delete (self,*args,**kwargs):
        super(product_entry,self).delete(*args,**kwargs)
        inintial_value = 0
        w = product_entry.objects.filter(Day = self.Day)
        for pe in w :
            inintial_value += pe.Total_price
        daily_sales.objects.filter(Day = self.Day).update(Total_sales=inintial_value)  

@receiver (post_save,sender=product_entry,)
def pe_calc (sender,instance,**kwargs):
    product_entry.objects.update(Total_price=F('Quantity')*F('Selling_price'))


#@receiver (post_init,sender=product_entry,)
#def implementer (sender,instance,**kwargs):
    #initial_quantity = 0
    #e = stock.objects.get(Item_Name=instance.)
    #stock.objects.filter(Item_Name=sender['product']).update(Quantity=F("sender['Quantity']")-F('Quantity')) 

    

    
    
     
    
   
    

   
    
              





class Receipts (models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=13)
    Date_sold = models.DateTimeField(auto_created=True)
    Overall_price = models.IntegerField(null = True,blank = True)
    def __str__(self):
        return self.Name
    class Meta :
        verbose_name_plural= 'Receipts'  

    def save(self,*args,**kwargs):
        super(Receipts,self).save(*args,**kwargs)
        







class Receipt_items (models.Model):
    
    Name = models.ForeignKey(Receipts,related_name='items',on_delete=models.CASCADE)
    Item = models.ForeignKey(stock,related_name='Name_items',on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Selling_price = models.IntegerField()
    Overall_item_price = models.IntegerField(null=True,blank=True)
    def save (self,*args,**kwargs):
        Receipt_items.objects.update(Overall_item_price=F('Quantity')*F('Selling_price'))
        super(Receipt_items,self).save(*args,**kwargs)
        initial_value = 0
        w = Receipt_items.objects.filter(Name = self.Name)
        for oip in w:
            initial_value += oip.Overall_item_price    
        Receipts.objects.filter(Name = self.Name).update(Overall_price=initial_value)
        y = Receipt_items.objects.filter(Name__Name=self.Name)
        for item in y :
            r = stock.objects.get(Item_Name=item.Item)
            remainder = r.Quantity - item.Quantity
            stock.objects.filter(Item_Name=item.Item).update(Quantity=remainder)
            stock.objects.update(overall_price=F('Quantity')*F('Selling_price'))


        super(Receipt_items,self).save(*args,**kwargs)

    def delete (self,*args,**kwargs):
        super(Receipt_items,self).delete(*args,**kwargs)
        inintial_value = 0
        w = Receipt_items.objects.filter(Name=self.Name)
        for pe in w :
            inintial_value += pe.Overall_item_price
        Receipts.objects.filter(Name = self.Name).update(Overall_price=inintial_value) 

@receiver (post_save,sender=Receipt_items)
def RI_calc (sender,instance,**kwargs):
    Receipt_items.objects.update(Overall_item_price=F('Quantity')*F('Selling_price')) 
              

    

