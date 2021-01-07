from django.contrib import admin
from stock.models import stock
from debts.models import items_debted_in, items_debted_out
from django.db.models import F
# Register your models here.

def calculate_overall_price (ModelAdmin,request,queryset):
    queryset.update(overall_price=F('Quantity')*F('Selling_price'))

class stockf(admin.ModelAdmin):
    change_list_template = 'admin/stock/change_list.html'

    def total_Cost_price(self):
        initial_value = 0
        q = stock.objects.all()
        for a in q :
            initial_value += a.Cost_price
        return initial_value 

    def total_Selling_price(self):
        initial_selling_value = 0
        q = stock.objects.all()
        for a in q :
            initial_selling_value += a.overall_price
        return initial_selling_value   

    def changelist_view(self,request,extra_content=None):
        #response = super().changelist_view(request)
        #try:
            #qs = response.context_data['cl'].queryset
        #except (AttributeError , KeyError) :
            #return response 
        my_context = {'total_Cost_price':self.total_Cost_price() , 'total_Selling_price':self.total_Selling_price() }
        #response.context_data['summary'] = list (qs)
        #return response      




        
        return super(stockf,self).changelist_view(request,my_context)             


    list_display = ['Item_Name','Quantity','Cost_price','Selling_price','date added','overall_price','Category']
    list_filter = ['Quantity','Category','date added']
    search_fields = ('Item_Name',)
    actions = [calculate_overall_price] 

    """def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="%s"/>' % obj.thumbnail.url
                )
        return "-"
        thumbnail_tag.short_description = "Thumbnail"  """
    

       

admin.site.register(stock,stockf)
