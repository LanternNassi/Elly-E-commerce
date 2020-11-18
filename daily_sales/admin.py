from django.contrib import admin
from daily_sales.models import daily_sales,product_entry,Receipt_items,Receipts
from stock.models import stock

# Register your models here.

class product_entry_admin (admin.TabularInline):
    model = product_entry
    extra = 3
    raw_id_fields = ('product',)


class daily_sales_admin (admin.ModelAdmin):
    fieldsets = [
        ('Day', {'fields':['Day']}),
        ('Date',{'fields':['Date_sold']}),
        ('Total_sales',{'fields':['Total_sales']}),
    ]    
    inlines = [product_entry_admin]
    search_fields = ('Day',)
    list_display = ('Day','Date_sold','Total_sales')
    list_filter = ('Date_sold','Day',)


class receipt_items (admin.TabularInline):
    model = Receipt_items
    raw_id_fields = ('Item',)

class receipt_admin (admin.ModelAdmin):
    fieldsets = [
        ('Details',{'fields':['Name','Email','Phone_number']}),
        ('Date Taken',{'fields':['Date_sold']}),
        ('Overall_item_price',{'fields':['Overall_price']})
    ]
    search_fields = ('Name',)
    inlines = [receipt_items]
    list_display = ('Name','Email','Phone_number','Date_sold','Overall_price')
    list_filter = ('Date_sold',)    



admin.site.register (daily_sales,daily_sales_admin)
admin.site.register (Receipts,receipt_admin)

        