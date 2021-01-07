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
from daily_sales.models import *
from daily_sales.admin import *

# Create your views here.

# function for rendering the home page (front-end)
def indexprovider(request):
    Plumbers = Plumbing_Services.objects.count()
    Tilers = Tiling_Services.objects.count()
    stock_no = stock.objects.count()
    return render(request,'elly/index.html',{'Plumbers':Plumbers,'Tilers':Tilers,'stock_no':stock_no})

#function for rendering the invoice
def admin_order_pdf (request,receipt_id):
	receipt = get_object_or_404 (Receipts,id=receipt_id)
	html = render_to_string('daily_sales/pdf.html',{'receipt':receipt})
	response = HttpResponse(content_type = 'application/pdf')
	response['Content-Disposition'] = 'filename = \"receipt_{}.pdf"'.format(receipt.id)
	weasyprint.HTML(string = html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
	return response

# function for calculating profits
def total_profits(id):
	p = product_entry.objects.filter(Day__id = id)
	initial = 0
	for e in p :
		if e.Profit < 0 :
			pass
		else :
			initial += e.Profit	
	return initial

# function for calculating losses
def losses(id):
	p = product_entry.objects.filter(Day__id = id)
	initial_loss = 0
	for e in p :
		if e.Profit < 0 :
			initial_loss += e.Profit
		else :
			pass
	return initial_loss			
			
# function for rendering the days report
def admin_report_pdf (request,Sale_id):
	'''Function for rendering the day's report'''
	Sale = daily_sales.objects.get(id = Sale_id)
	profit = total_profits(Sale_id)
	loss = losses(Sale_id)
	html = render_to_string('daily_sales/Daily Sales/pdf.html',{'Sale':Sale,'profit':profit,'loss':loss})
	response = HttpResponse(content_type = 'application/pdf')
	response['Content-Disposition'] = 'filename = \"Sale_{}.pdf"'.format(Sale.id)
	weasyprint.HTML(string = html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
	return response


       
    



    


