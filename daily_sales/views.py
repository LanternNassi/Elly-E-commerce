from django.shortcuts import render,get_object_or_404
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
import weasyprint
from django.utils.html import format_html
from weasyprint import HTML
import tempfile
from Services.models import Plumbing_Services,Tiling_Services
from stock.models import stock
from daily_sales.models import Receipts, Receipt_items

# Create your views here.




def indexprovider(request):
    Plumbers = Plumbing_Services.objects.count()
    Tilers = Tiling_Services.objects.count()
    stock_no = stock.objects.count()
    return render(request,'elly/index.html',{'Plumbers':Plumbers,'Tilers':Tilers,'stock_no':stock_no})


def admin_order_pdf (request,receipt_id):
	receipt = get_object_or_404 (Receipts,id=receipt_id)
	html = render_to_string('daily_sales/pdf.html',{'receipt':receipt})
	response = HttpResponse(content_type = 'application/pdf')
	response['Content-Disposition'] = 'filename = \"receipt_{}.pdf"'.format(receipt.id)
	weasyprint.HTML(string = html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
	return response

       
    



    


