from django.shortcuts import render
from Services.models import Plumbing_Services,Tiling_Services
from stock.models import stock

# Create your views here.




def indexprovider(request):
    Plumbers = Plumbing_Services.objects.count()
    Tilers = Tiling_Services.objects.count()
    stock_no = stock.objects.count()
    return render(request,'elly/index.html',{'Plumbers':Plumbers,'Tilers':Tilers,'stock_no':stock_no})
    
