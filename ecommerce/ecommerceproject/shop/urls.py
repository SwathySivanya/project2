from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ecommerceproject import settings
app_name='shop'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proCatdetail'),
]