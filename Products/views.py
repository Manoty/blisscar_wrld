from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from .models import Product
from .credentials import *
from django.http import HttpResponse
# Create your views here.

def products(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, 'Products/products.html', context)

def add_products(request):
    if request.method =="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfully')
            return redirect("add-products-url")
        else:
            messages.error(request, 'Product saving failed')
            return redirect("add-products-url")
    else:
        form = ProductForm()
    return render(request, 'Products/add-products.html', {'form': form})


def update_products(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product_name = request.POST.get('name')
        product_year = request.POST.get('year')
        product_transmission = request.POST.get('transmission')
        product_price = request.POST.get('price')
        product_image = request.POST.get('image')
        product.name = product_name
        product.year = product_year
        product.transmission = product_transmission
        product.price = product_price
        product.image = product_image
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                product.save()
                messages.success(request,'Product updated succcesfully')
                return redirect('products-url')


    return render(request, 'Products/update-product.html', {'product':product})

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('products-url')


def pay(request, id):
    product = Product.objects.get(id=id)



    if request.method == "POST":
        phone = request.POST['phone']
        amount = product.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "School fees"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("success")
    return render(request, 'products/pay.html', {'product': product})


