from django.db import models
from stock.models import stock

# Create your models here.

class Order (models.Model):
	first_name=models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	class Meta :
		ordering = ('-created',)
	def __str__(self):
		return 'Order {}'.format(self.id)
	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
	product = models.ForeignKey(stock,related_name='order_items',on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField()
	
	def __str__(self):
		return '{}'.format(self.id)
	def get_cost(self):
		return self.price * self.quantity
		
