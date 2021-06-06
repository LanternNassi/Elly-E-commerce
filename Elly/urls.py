"""Elly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,URLPattern,reverse
from django.conf import settings
from Elly import settings
from django.conf.urls import include,static,url
from django.conf.urls.static import static
from Services.views import recorder,login_view,recorder_tiler,login_view_tiler,services_renderer,profile_renderer,profile_renderer_plumbing,tiler_editer,plumber_editer
from daily_sales.views import indexprovider
from stock.views import *
from cart import views
from orders.views import order_create, admin_order_pdf




urlpatterns = [
    path('admin/', admin.site.urls),

#url(r'^cart/',include('cart.urls',namespace='cart')),
  
    
    path('',indexprovider,name='index'),
    path('Catalogue/',catalogue_view, name='catalogue'),
    path('services_plumber/',recorder,name='service'),
    path('login_plumber/',login_view,name='p_login'),
    path('login_tiler/',login_view_tiler,name='service_tiler'),
    path('Tiler_signup/',recorder_tiler,name='t_service'),
    path('object/<int:pk>/',individual_catalogue_view,name='item'),
    path('services/',services_renderer,name='services'),
    path('service_profile/<int:id>/',profile_renderer, name='profile'),
    path('plumber_profile/<int:id>/',profile_renderer_plumbing,name='p_profile'),
    path('plumber_account/',login_view,name='plumber_account'),
    path('Tiler_account/',login_view_tiler,name='tiler_account'),
    url('cart/',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add,name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$',views.cart_remove,name='cart_remove'),
    #url(r'^', include('Elly.urls', namespace='Elly')),
    # shopping cart urls
    url(r'^create/$',order_create,name='order_create'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$',admin_order_pdf,name='admin_order_pdf'),
    path('tiler/<int:id>/edit/',tiler_editer,name='tiler_editer'),

    path('tiles/',tiles_category_view,name='tcv'),
    path('plumbing_gallery/',plumbing_category_view,name='pcv'),
    path('bathroom_accessories/',bathroom_accessories_category_view,name='bcv'),
    path('plumber/<int:id>/edit',plumber_editer,name='plumber_editer'),


    
    

     
    

] 
#url(r'^cart/',include('cart.urls',namespace=INSTALLED_APPS[11])),

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



#for app in settings.INSTALLED_APPS:
    #urlpatterns += urlpatterns('',url(r'^cart/'.format(app),include(app+'.urls',namespace=app)))
