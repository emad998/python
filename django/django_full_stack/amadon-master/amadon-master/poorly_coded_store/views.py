from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    if "entireCharge" not in request.session:
        request.session['entireCharge'] = 0

    if "entireItems" not in request.session:
        request.session['entireItems'] = 0    
    
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkoutPage(request):
    productChosen = Product.objects.get(id=request.POST["product_id"])
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(productChosen.price)
    total_charge = quantity_from_form * price_from_form
    request.session['entireCharge'] += total_charge
    request.session['entireItems'] += quantity_from_form
    
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    return redirect('/checkout')
    

def checkout(request):
    return render(request, "store/checkout.html")
