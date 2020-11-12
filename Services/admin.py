from django.contrib import admin
from Services.models import Plumbing_Services,Tiling_Services,images_plumbing,images_tiling

# Register your models here.

class plumbing_images (admin.StackedInline):
    model = images_plumbing

class tiling_images (admin.StackedInline):
    model = images_tiling    



class PlumbingServices (admin.ModelAdmin):
    list_display=['Name','Contact','Status','EMail']
    search_fields = ('Name',)
    fieldsets= [
        ('Details',{'fields':['Name','Password','Contact','Status','EMail','profile_pic']}),
        
    ]
    inlines=[plumbing_images]
    

class Tilingservices (admin.ModelAdmin):
    list_display = ['Name','Contact','Status','Email'] 
    search_fields = ['Name',]
    fieldsets= [
        ('Details',{'fields':['Name','Password','Contact','Status','Email','profile_pic']}),
        
    ]  
    inlines=[tiling_images]




admin.site.register(Plumbing_Services,PlumbingServices)
admin.site.register(Tiling_Services,Tilingservices)

