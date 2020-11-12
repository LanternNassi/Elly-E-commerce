from django.contrib import admin
from debts.models import debts_in , debts_out, items_debted_in, items_debted_out,situation_in,situation_out
from stock.models import stock
from django.db.models import F


# Register your models here.

#choices function
def status_updater_1 (ModelAdmin,request,queryset):
    queryset.update(situation='p')
status_updater_1.short_description = "Mark selected items Paid"

def status_updater_2 (ModelAdmin,request,queryset):
    queryset.update(situation='N')
status_updater_2.short_description = "Mark selected items not paid"

def clearance_updater_1 (ModelAdmin,request,queryset):
    queryset.update(clearance='Y')
clearance_updater_1.short_description = 'Mark them cleared'

def clearance_updater_2 (ModelAdmin,request,queryset):
    queryset.update(clearance='N')
clearance_updater_2.short_description='Not yet cleared' 

def overall_price_item (ModelAdmin,request,queryset):
    queryset.update(Overall_item_price=F('Quantity')*F('Price'))
overall_price_item.short_description='Calculate overall price item'    

class debtedin(admin.TabularInline):
    model = items_debted_in
    autocomplete_fields = ('item',)


class in_situation (admin.TabularInline):
    model = situation_in



class QuestionAdmin_debts_in(admin.ModelAdmin):
    fieldsets = [
        ('Name',   {'fields': ['Name']}),
        ('Date information', {'fields': ['Date Taken'], 'classes':['collapse']}),
        ('Overall ', {'fields':['Overall_price','Paid','Balance']}),
        ('situation',{'fields':['situation']}),

    ]
    inlines = [in_situation,debtedin]
    list_display = ('Name','Date Taken','situation','clearance','Overall_price','Paid','Balance')
    actions = [clearance_updater_1,clearance_updater_2,overall_price_item]
    search_fields = ('Name',)
    


class debtedout(admin.TabularInline):
    model = items_debted_out
    autocomplete_fields = ('item',)


class out_situation (admin.TabularInline):
    model = situation_out
        
    

class Questionadmin_debts_out(admin.ModelAdmin):
    fieldsets = [
        ('Name',   {'fields': ['Name']}),
        ('Date information', {'fields': ['Date Taken'], 'classes':['collapse']}),
        ('Overall', {'fields':['Overall_price','Paid','Balance']}),
        ('situation',{'fields':['situation']}),

    ]
    inlines = [out_situation,debtedout]
    list_display = ('Name','Date Taken','situation','clearance','Overall_price','Paid','Balance')
    actions = [clearance_updater_1,clearance_updater_2,overall_price_item]
    search_fields = ('Name',)
    

   
    
admin.site.register(debts_in, QuestionAdmin_debts_in )
admin.site.register(debts_out, Questionadmin_debts_out)
