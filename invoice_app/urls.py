from django.urls import path
from invoice_app import views

urlpatterns = [

    # path('', views.base, name = 'base' ),
    path('', views.home, name= "home"),
    path('index/', views.index, name ='index'),
    path('form/', views.form, name='form'),
    path('orderForm/', views.orderForm, name= 'orderForm')

    
]