from django.shortcuts import render
from stock.models import stock
from cart.forms import CartAddProductForm

# Create your views here.


def catalogue_view (request):
    stock_catalogue = stock.objects.all()
    plumbingf = stock.objects.filter(Category='Plumbing')
    bathroom_accessoriesf = stock.objects.filter(Category='Bathroom accessories')
    tilesf = stock.objects.filter(Category='Tiles')
    return render(request,'elly/portfolio.html',{'tag':stock_catalogue,'plumbing':plumbingf,'ba':bathroom_accessoriesf,'tiles':tilesf})

def individual_catalogue_view (request,pk):
    stock_solo = stock.objects.get(pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request,'elly/portfolio-details.html',{'stock_solo':stock_solo,'cart_product_form':cart_product_form})    