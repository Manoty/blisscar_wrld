
from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.products, name='products-url'),
    path('add-products/', my_views.add_products, name='add-products-url'),
    path('delete/<int:id>/', my_views.delete, name='delete-url'),
    path('update/<int:id>/', my_views.update_products, name='update_url'),
    path('pay/<int:id>/', my_views.pay, name='pay_url')
]