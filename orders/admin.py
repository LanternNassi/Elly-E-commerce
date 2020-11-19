from django.contrib import admin
from orders.models import Order,OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']
	
class OrderAdmin(admin.ModelAdmin):
	
	list_filter = ['paid','created','updated']
	inlines = [OrderItemInline]
	
	def order_pdf(obj):
		return '<a href = "{}">PDF</a>'.format(
			reverse('orders:admin_order_pdf',args=[obj.id])
		)

		

	order_pdf.allow_tags = True
	order_pdf.short_description = 'PDF bill'

	list_display = ['id','first_name','last_name','email','address','paid','created','updated',order_pdf]	

admin.site.register(Order,OrderAdmin)	
	
		
	
