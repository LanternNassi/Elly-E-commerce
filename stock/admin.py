from django.contrib import admin
from stock.models import stock
from debts.models import items_debted_in, items_debted_out
from django.db.models import F
# Register your models here.

def calculate_overall_price (ModelAdmin,request,queryset):
    queryset.update(overall_price=F('Quantity')*F('Selling_price'))

class stockf(admin.ModelAdmin):
    list_display = ['Item_Name','Quantity','Cost_price','Selling_price','date added','overall_price','Category']
    list_filter = ['Quantity','Category']
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
