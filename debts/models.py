from django.db import models

from django.db.models import F
from django.dispatch import Signal,receiver
from django.db.models.signals import post_save
from daily_sales.models import * 
from stock.models import stock



# Create your models here.

status_choices = [
    ('p','Paid'),
    ('N','Not paid'),
]

clearances = [
    ('Y','Cleared'),
    ('N','Not cleared')
]

class debts_in(models.Model):
    Name = models.CharField(max_length=10)
    Date_added = models.DateTimeField(name='Date Taken',auto_now_add=False)
    Overall_price = models.IntegerField(null=True,blank=True)
    Paid = models.IntegerField(null = True,blank = True)
    Balance = models.IntegerField(null = True,blank = True)
    clearance = models.CharField(max_length=1 , choices=clearances)
    situation = models.BooleanField(name= 'situation',default=False,editable=True)
    class Meta():
        verbose_name_plural = 'debts in'
    def __str__(self):
        return self.Name

      
        

class situation_in (models.Model):
    Name = models.ForeignKey(debts_in,on_delete=models.CASCADE)
    Day = models.CharField(max_length=10)
    Date_paid = models.DateTimeField(auto_created=True)
    Amount_paid = models.IntegerField()
    def save (self,*args,**kwargs):
        super(situation_in,self).save(*args,**kwargs)
        w = situation_in.objects.filter(Name=self.Name)
        initial_value = 0
        for pe in w :
            initial_value += pe.Amount_paid
        debts_in.objects.filter(Name = self.Name).update(Paid=initial_value,Balance=F('Overall_price')-initial_value)
        # deductiing the money from the daily sales 
        e = daily_sales.objects.filter(Day = "Today")
        for p in e :
            remainder = p.Total_sales - self.Amount_paid
        daily_sales.objects.filter(Day = "Today").update(Total_sales = remainder )

        

        super(situation_in,self).save(*args,**kwargs)

    def delete (self,*args,**kwargs):
        super(situation_in,self).delete(*args,**kwargs)
        w = situation_in.objects.filter(Name=self.Name)
        initial_value = 0 
        for pe in w :
            initial_value += pe.Amount_paid
        debts_in.objects.filter(Name = self.Name).update(Paid = initial_value,Balance = F('Overall_price')-initial_value)




# the debts out class
    
class debts_out (models.Model):
    Name = models.CharField(max_length=10)
    Date_added = models.DateTimeField(name='Date Taken', auto_now_add=False)
    Overall_price = models.PositiveIntegerField(null=True,blank=True)
    Paid = models.IntegerField(null = True,blank = True)
    Balance = models.IntegerField(null = True,blank=True)
    clearance = models.CharField(max_length=1 , choices=clearances)
    situation = models.BooleanField(default=False, editable=True)
    class Meta():
        verbose_name_plural='debts out'
    def __str__(self):
        return self.Name


class situation_out (models.Model):
    Name = models.ForeignKey(debts_out,on_delete=models.CASCADE)
    Day = models.CharField(max_length=10) 
    Date_paid = models.DateTimeField(auto_created=True)
    Amount_paid = models.IntegerField()
    def save (self,*args,**kwargs):
        super(situation_out,self).save(*args,**kwargs)
        w = situation_out.objects.filter(Name=self.Name) 
        initial_value = 0
        for pe in w :
            initial_value += pe.Amount_paid
        debts_out.objects.filter(Name = self.Name).update(Paid=initial_value,Balance=F('Overall_price')-initial_value)

        # adding the paid money to the daily sales

        e = daily_sales.objects.filter(Day = "Today")
        for p in e :
            remainder = p.Total_sales + self.Amount_paid
        daily_sales.objects.filter(Day = "Today").update(Total_sales = remainder )

        super(situation_out,self).save(*args,**kwargs)    
    

    def delete (self,*args,**kwargs):
        super(situation_out,self).delete(*args,**kwargs)
        w = situation_out.objects.filter(Name=self.Name)
        initial_value = 0 
        for pe in w :
            initial_value += pe.Amount_paid
        credit.objects.filter(Name = self.Name).update(Paid = initial_value,Balance = F('Overall_price')-initial_value)
    

           
    
# the fill in class
        
class items_debted_in(models.Model):
    Name = models.ForeignKey(debts_in, on_delete=models.CASCADE)
    item = models.ForeignKey(stock,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Overall_item_price = models.IntegerField(null=True,blank=True) 
    situation_2 = models.BooleanField(default=True) 
    def save (self,*args,**kwargs):
        items_debted_in.objects.update(Overall_item_price=F('Quantity')*F('Price'))
        super(items_debted_in,self).save(*args,**kwargs)
        initial_value = 0
        w = items_debted_in.objects.filter(Name=self.Name)
        for oip in w:
            initial_value += oip.Overall_item_price
        debts_in.objects.filter(Name=self.Name).update(Overall_price = initial_value)        
        super(items_debted_in,self).save(*args,**kwargs)

    def delete (self,*args,**kwargs):
        super(items_debted_in,self).delete(*args,**kwargs)
        initial_value = 0
        w = items_debted_in.objects.filter(Name=self.Name)
        for pe in w :
            initial_value += pe.Overall_item_price
        debts_in.objects.filter(Name = self.Name).update(Overall_price=initial_value)        


@receiver(post_save,sender=items_debted_in)
def debt_calc (sender,instance,**kwargs):
    items_debted_in.objects.update(Overall_item_price=F('Quantity')*F('Price'))
   
    
    
    


class items_debted_out(models.Model):
    Name = models.ForeignKey(debts_out, on_delete=models.CASCADE)
    item = models.ForeignKey(stock,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Overall_item_price = models.IntegerField(null=True,blank=True)
    situation_2 = models.BooleanField(default=True)
    def save (self,*args,**kwargs):
        items_debted_out.objects.update(Overall_item_price=F('Quantity')*F('Price'))
        super(items_debted_out,self).save(*args,**kwargs)
        initial_value = 0
        w = items_debted_out.objects.filter(Name = self.Name)
        for oip in w:
            initial_value += oip.Overall_item_price
        debts_out.objects.filter(Name=self.Name).update(Overall_price = initial_value)
        super(items_debted_out,self).save(*args,**kwargs)

    def delete (self,*args,**kwargs):
        super(items_debted_out,self).delete(*args,**kwargs)
        initial_value = 0
        w = items_debted_out.objects.filter(Name = self.Name)
        for pe in w :
            initial_value += pe.Overall_item_price
        debts_out.objects.filter(Name = self.Name).update(Overall_price=initial_value)        

@receiver(post_save,sender=items_debted_out)
def debtout_calc (sender,instance,**kwargs):
    items_debted_out.objects.update(Overall_item_price=F('Quantity')*F('Price'))        
   

class undefined_debts (models.Model):
    Name = models.CharField(max_length =100)   
    Phone = models.CharField( max_length=50)
    Date = models.DateTimeField( auto_now=False, auto_now_add=False)
    Amount = models.IntegerField()
    Paid = models.IntegerField(null = True,blank = True)
    Balance = models.IntegerField(null = True,blank=True)
    clearance = models.CharField(max_length=1 , choices=clearances)
    situation = models.BooleanField(default=False, editable=True)

    
    def __str__(self):
        return self.Name


class undefined_debts_situation (models.Model):
    Name = models.ForeignKey(undefined_debts,on_delete=models.CASCADE)
    Day = models.CharField(max_length=10)
    Date_paid = models.DateTimeField(auto_created=True)
    Amount_paid = models.IntegerField()
    def save (self,*args,**kwargs):
        super(undefined_debts_situation,self).save(*args,**kwargs)
        w = undefined_debts_situation.objects.filter(Name__Name=self.Name)
        initial_value = 0
        q = undefined_debts.objects.get(Name = self.Name)
        for pe in w :
            initial_value += pe.Amount_paid
        undefined_debts.objects.filter(Name = self.Name).update(Paid=initial_value,Balance=q.Amount-initial_value)
        super(undefined_debts_situation,self).save(*args,**kwargs)





class undefined_credit (models.Model):
    Name = models.CharField(max_length =100)   
    Phone = models.CharField( max_length=50)
    Date = models.DateTimeField( auto_now=False, auto_now_add=False)
    Amount = models.IntegerField()
    Paid = models.IntegerField(null = True,blank = True)
    Balance = models.IntegerField(null = True,blank=True)
    clearance = models.CharField(max_length=1 , choices=clearances)
    situation = models.BooleanField(default=False, editable=True)
    def __str__(self):
        return self.Name


class undefined_credit_situation (models.Model):
    Name = models.ForeignKey(undefined_credit,on_delete=models.CASCADE)
    Day = models.CharField(max_length=10)
    Date_paid = models.DateTimeField(auto_created=True)
    Amount_paid = models.IntegerField()     
    def save (self,*args,**kwargs):
        super(undefined_credit_situation,self).save(*args,**kwargs)
        w = undefined_credit_situation.objects.filter(Name__Name=self.Name)
        initial_value = 0
        q = undefined_credit.objects.get(Name = self.Name)
        for pe in w :
            initial_value += pe.Amount_paid
        undefined_credit.objects.filter(Name = self.Name).update(Paid=initial_value,Balance=q.Amount-initial_value)
        super(undefined_credit_situation,self).save(*args,**kwargs)   
            
    