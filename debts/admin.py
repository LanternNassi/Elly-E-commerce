from django.contrib import admin
from debts.models import *
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
    

class undefined_credit_situation_inline (admin.TabularInline):
    model = undefined_credit_situation

class undefined_credit_admin(admin.ModelAdmin):
    change_list_template = 'admin/debts/credits/change_list.html'
    
    def total_credit (self):
        initial_credit_value = 0
        w = undefined_credit.objects.all()
        for p in w :
            initial_credit_value += p.Amount
        return initial_credit_value    


    def changelist_view (self,request,extra_content = None):
        my_context = {'total_credit': self.total_credit}
        return super(undefined_credit_admin,self).changelist_view(request,my_context)


    fieldsets = [
        ('Name',   {'fields': ['Name']}),
        ('Date information', {'fields': ['Date'], 'classes':['collapse']}),
        ('Overall', {'fields':['Amount','Paid','Balance']}),
        ('situation',{'fields':['situation']}),

    ]
    inlines = [undefined_credit_situation_inline]
    list_display = ('Name','Date','situation','clearance','Amount','Paid','Balance')
    actions = [clearance_updater_1,clearance_updater_2]
    search_fields = ('Name',)



    
class undefined_debts_situation_inline (admin.TabularInline):
    model = undefined_debts_situation

class undefined_debts_admin(admin.ModelAdmin):
    change_list_template = 'admin/debts/debts/change_list.html'
    def total_debts(self):
        initial_value = 0 
        w = undefined_debts.objects.all()
        for p in w :
            initial_value += p.Amount
        return initial_value

            
    def changelist_view (self,request,extra_content = None):
        my_context = {'total_debts': self.total_debts}
        return super(undefined_debts_admin,self).changelist_view(request,my_context)


    fieldsets = [
        ('Name',   {'fields': ['Name']}),
        ('Date information', {'fields': ['Date'], 'classes':['collapse']}),
        ('Overall', {'fields':['Amount','Paid','Balance']}),
        ('situation',{'fields':['situation']}),

    ]
    inlines = [undefined_debts_situation_inline]
    list_display = ('Name','Date','situation','clearance','Amount','Paid','Balance')
    actions = [clearance_updater_1,clearance_updater_2]
    search_fields = ('Name',)



    
admin.site.register(debts_in, QuestionAdmin_debts_in )
admin.site.register(debts_out, Questionadmin_debts_out)
admin.site.register(undefined_credit, undefined_credit_admin)
admin.site.register(undefined_debts, undefined_debts_admin)
