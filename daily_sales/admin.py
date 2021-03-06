from django.contrib import admin
from django.shortcuts import render,get_object_or_404
from django.conf.urls import url
from django.urls import path,URLPattern,reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import format_html
from weasyprint import HTML
import tempfile
from .views import *
from daily_sales.models import daily_sales,product_entry,Receipt_items,Receipts
from stock.models import stock
#from daily_sales.views import InvoiceMixin
# Register your models here.

class product_entry_admin (admin.TabularInline):
    model = product_entry
    extra = 3
    raw_id_fields = ('product',)

# daily sales admin customisation
class daily_sales_admin (admin.ModelAdmin):
    change_form_template = 'admin/daily_sales/Daily Sales/change_form.htm'
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "Report/<int:Sale_id>/",
                self.admin_site.admin_view(admin_report_pdf ),
                name="sale",
            )
        ]
        return my_urls + urls

   # Calculating the daily profits 
    def profits (obj):
        initial_value = 0
        d = product_entry.objects.filter(Day__Day = obj.Day)
        for e in d :
            initial_value += e.Profit
        return initial_value 

    profits.shortdescription = "Total Profit"

    fieldsets = [
        ('Day', {'fields':['Day']}),
        ('Date',{'fields':['Date_sold','Approved']}),
        ('Total_sales',{'fields':['Total_sales']}),
    ]    
    inlines = [product_entry_admin]
    search_fields = ('Day',)
    list_display = ('Day','Date_sold','Approved','Total_sales',profits)
    list_filter = ('Date_sold','Day',)


class receipt_items (admin.TabularInline):
    model = Receipt_items
    raw_id_fields = ('Item',)

class receipt_admin (admin.ModelAdmin):
    change_form_template = 'admin/daily_sales/Receipts/change_form.html'
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "invoice/<int:receipt_id>/",
                self.admin_site.admin_view(admin_order_pdf ),
                name="invoice",
            )
        ]
        return my_urls + urls


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

        