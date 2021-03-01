from django.db import models
import django.dispatch 
from django.dispatch import receiver
from django.db.models.signals import post_init,pre_init,pre_save,post_save
from django.db.models import F
from stock.models import stock
import json
from datetime import date 


# Create your models here
# 
# .




class daily_sales (models.Model):
    Day = models.CharField(max_length=10)
    Date_sold = models.DateTimeField(auto_now_add=False )
    Approved = models.BooleanField(default = False)
    Total_sales = models.IntegerField(null=True,blank = True)
    class Meta():
        verbose_name_plural='daily sales'
    def __str__(self):
        return self.Day
    def save(self,*args,**kwargs):
        super(daily_sales,self).save(*args,**kwargs)
        inintial_value = 0
        w = product_entry.objects.filter(Day__Day=self.Day)
        for p in w :
            inintial_value += p.Total_price
        super(daily_sales,self).save(*args,**kwargs)
        daily_sales.objects.filter(Day = self.Day).update(Total_sales=inintial_value)
    



class product_entry (models.Model):
    Day = models.ForeignKey(daily_sales,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(stock,related_name='Day_items',on_delete=models.CASCADE)
    Quantity = models.IntegerField(null = True,blank = True)    
    Selling_price = models.IntegerField(null = True,blank = True)
    Total_price = models.IntegerField(null = True,blank = True)
    Profit = models.IntegerField(null = True, blank = True)
    def save (self,*args,**kwargs):
        product_entry.objects.update(Total_price=F('Quantity')*F('Selling_price'))
        super(product_entry,self).save(*args,**kwargs)
        # Updating the profits
        e = stock.objects.filter(Item_Name = self.product)
        for w in e :
            profit = self.Selling_price - w.Cost_price
        product_entry.objects.filter(product = self.product).update(Profit = self.Quantity*profit)
        # Calculating total sales
        #inintial_value = 0
        #w = product_entry.objects.filter(Day=self.Day)
        #for p in w : 
         #   inintial_value += p.Total_price
        #daily_sales.objects.filter(Day = self.Day).update(Total_sales=inintial_value)  
        #super(product_entry,self).save(*args,**kwargs)
        stock.objects.update(overall_price=F('Quantity')*F('Selling_price'))
        
 
    def delete (self,*args,**kwargs):
        #e = stock.objects.get(Item_Name=self.product__items)  
        #total = e.Quantity + self.Quantity
        #stock.objects.filter(Item_Name=self.product__items).update(Quantity=total)
        inintial_value = 0
        w = product_entry.objects.filter(Day = self.Day)
        for pe in w :
            inintial_value += pe.Total_price
        daily_sales.objects.filter(Day = self.Day).update(Total_sales=inintial_value)
        super(product_entry,self).delete(*args,**kwargs)

# ==================================================  END OF DAILY SALES APP SECTION =========================================        
    

#@receiver (post_save,sender=product_entry,)
#def pe_calc (sender,instance,**kwargs):
    #product_entry.objects.update(Total_price=F('Quantity')*F('Selling_price'))


#===================================================  RECEIPTS APP SECTION ===================================================

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
        
# Class for adding receipt items(tabularinline)
class Receipt_items (models.Model):
    Name = models.ForeignKey(Receipts,related_name='items',on_delete=models.CASCADE)
    Item = models.ForeignKey(stock,related_name='Name_items',on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Selling_price = models.IntegerField(null = True , blank = True)
    Overall_item_price =  models.IntegerField(blank = True, null = True)
    #Overiding the save function{ To calculate the overall item price of each item , To update the stock database about the items sold }
    def save (self,*args,**kwargs):
        super(Receipt_items,self).save(*args,**kwargs)
        # Calculating the overall item price
        Receipt_items.objects.update(Overall_item_price=F('Quantity')*F('Selling_price'))
        #super(Receipt_items,self).save(*args,**kwargs)
        initial_value = 0
        w = Receipt_items.objects.filter(Name = self.Name)
        for oip in w:
            initial_value += oip.Overall_item_price    
        Receipts.objects.filter(Name = self.Name).update(Overall_price=initial_value)
        r = stock.objects.get(Item_Name=self.Item)
        remainder = r.Quantity - self.Quantity
        #updating the stock database about the items sold
        stock.objects.filter(Item_Name = self.Item ).update(Quantity=remainder)
        # reveryifing the calcualations in the database
        stock.objects.update(overall_price=F('Quantity')*F('Selling_price')) 
        #adding receipt items to daily sales
        obj,identifier = daily_sales.objects.get_or_create(Day="Today",Date_sold=date.today())
        product_entry.objects.create(Day=obj ,product=self.Item,Quantity=self.Quantity,Selling_price=self.Selling_price,Total_price=self.Overall_item_price)
        super(Receipt_items,self).save(*args,**kwargs)

    def delete (self,*args,**kwargs):
        e = stock.objects.get(Item_Name = self.Item)
        total = e.Quantity + self.Quantity
        stock.objects.filter(Item_Name=self.Item).update(Quantity=total)
        super(Receipt_items,self).delete(*args,**kwargs)
        inintial_value = 0
        w = Receipt_items.objects.filter(Name=self.Name)
        for pe in w :
            inintial_value += pe.Overall_item_price
        Receipts.objects.filter(Name = self.Name).update(Overall_price=inintial_value) 

@receiver (post_save,sender=Receipt_items)
def RI_calc (sender,instance,**kwargs):
    Receipt_items.objects.update(Overall_item_price=F('Quantity')*F('Selling_price')) 


    # =======================================================================  END OF RECEIPTS ITEMS SECTION  =================================================================
              

    

