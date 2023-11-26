from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request, 'Products/products.html')

def add_products(request):
    return render(request, 'Products/add-products.html')

def update_products(request):
    return render(request, 'Products/update-product.hwhattml')