from django.contrib import admin
from django.urls import path,URLPattern,reverse
from orders.models import Order,OrderItem
from django.http import HttpResponse
from orders.views import  admin_order_pdf
from django.utils.html import mark_safe

# Register your models here.

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']


def order_pdf(obj):
	return mark_safe ('<a href="{}">PDF</a>'.format(
		reverse('admin_order_pdf',args=[obj.id])
	))
	
order_pdf.allow_tags = True
order_pdf.short_description = 'PDF bill'

class OrderAdmin(admin.ModelAdmin):
	
	list_filter = ['paid','created','updated']
	inlines = [OrderItemInline]
	

	list_display = ['id','first_name','last_name','email','address','paid','created','updated',order_pdf]	

admin.site.register(Order,OrderAdmin)	
	
		
	
