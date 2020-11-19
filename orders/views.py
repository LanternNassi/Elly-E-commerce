from django.shortcuts import render
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import OrderItem
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

# Create your views here.

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart :
				OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
			cart.clear()
			return render(request,'orders/order/created.html',{'order':order})
	else:
		form = OrderCreateForm()
	return render(request,'orders/order/create.html',{'cart':cart,'form':form})	



@staff_member_required
def admin_order_pdf (request,order_id):
	order = get_object_or_404 (Order,id=order_id)
	html = render_to_string('orders/order/pdf.html',{'order':order})
	response = HttpResponse(content_type = 'application/pdf')
	response['Content-Disposition'] = 'filename = \"order_{}.pdf"'.format(order.id)
	weasyprint.HTML(string = html).write_pdf(response,stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
	return response