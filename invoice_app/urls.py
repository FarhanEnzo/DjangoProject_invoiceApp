from django.urls import path
from invoice_app import views

urlpatterns = [

    path('', views.home, name = "home"),
    path('index/', views.index, name = 'index'),
    path('form/', views.form, name = 'form'),
    path('orderForm/', views.orderForm, name = 'orderForm'),
    path('sold_list/<int:item_id>/', views.sold_list, name = 'sold_list'),
    path('edit_info/<int:food_id>/', views.edit_info, name = 'edit_info'),
    path('delete_info/', views.delete_info, name ='delete_info'),

]

