from django.db.models.signals import post_init,pre_init
from django.dispatch import receiver

from stock.models import stock

from .models import product_entry,daily_sales

@receiver(pre_init,sender=daily_sales)
def autofill(sender,**kwargs):
        b = kwargs
        reference = b['product']
        s = stock.objects.get(Item_Name=reference)
        product_entry.objects.create(Day=b['Day'],product=b['product'],Quantity=s.Quantity,Selling_price=s.Selling_price,Total_price=s.overall_price)


