from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

import bcrypt

from .models import User, Food, Order





# Create your views here.
def index(request):
    return render(request, "index.html")

def regUpdate(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['passwordLabel']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        created_user = User.objects.create(
            first_name = request.POST['firstNameLabel'],
            last_name = request.POST['lastNameLabel'],
            email = request.POST['emailLabel'],
            password = pw_hash
        )

        request.session['userid'] = created_user.id
        request.session['userName'] = created_user.first_name
        return redirect('/success')

def loginProcess(request):
    user = User.objects.filter(email=request.POST['emailLabel'])
    if len(user) == 0:
        messages.error(request, "Please check your email and password")
        return redirect("/")
    if bcrypt.checkpw(request.POST['passwordLabel'].encode(), user[0].password.encode()):
        request.session['userid'] = user[0].id
        request.session['userName'] = user[0].first_name
        return redirect("/success")
        
    else:
        messages.error(request, "Please check your email and password")
        return redirect("/")
    


def successView(request):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    elif request.session['userid'] == 1:
        if 'entireCharge' not in request.session:
            request.session['entireCharge'] = 0
        if 'entireItems' not in request.session:
            request.session['entireItems'] = 0
        if 'entireCalories' not in request.session:
            request.session['entireCalories'] = 0

        context = {
            'all_foods': Food.objects.all()
        }
        return render(request, "success.html", context)

    else:
        if 'entireCharge' not in request.session:
            request.session['entireCharge'] = 0
        if 'entireItems' not in request.session:
            request.session['entireItems'] = 0
        if 'entireCalories' not in request.session:
            request.session['entireCalories'] = 0

        context = {
            'all_foods': Food.objects.all()

        }
        return render(request, "item-dashboard.html", context)


def loggingOut(request):
    request.session.clear()
    return redirect('/')



# ---------create food section ---------
def createView(request):


    return render(request, 'create.html')


# ---------createing a food form  ---------

def realCreating(request):
    Food.objects.create(

    food_name = request.POST['foodNameLabel'],
    price = request.POST['priceLabel'],
    calories = request.POST['caloriesLabel'],
    fat = request.POST['fatsLabel'],
    carbs = request.POST['carbsLabel'],
    fiber = request.POST['fiberLabel'],
    protein = request.POST['proteinLabel'],
    image = request.POST['imageLabel'],

    user_favorite = User.objects.get(id=request.session['userid'])

    )
    return redirect ('/success')


# edit page view -----------------

def edit_pageView(request, id):

    context = {
        'item_to_edit': Food.objects.get(id=id)  

    }
    return render(request, 'edit.html', context)

#real edit page now ------------------

def real_editing(request, id2):

    edited_item = Food.objects.get(id=id2)

    edited_item.food_name = request.POST['foodNameLabel']
    edited_item.price = request.POST['priceLabel']
    edited_item.calories = request.POST['caloriesLabel']
    edited_item.fat = request.POST['fatsLabel']
    edited_item.carbs = request.POST['carbsLabel']
    edited_item.fiber = request.POST['fiberLabel']
    edited_item.protein = request.POST['proteinLabel']
    edited_item.image = request.POST['imageLabel']

    edited_item.save()

    return redirect ('/success')

# delete functionality -----------------
def destroy(request, id3):
    deleted_food = Food.objects.get(id=id3)
    deleted_food.delete()

    return redirect('/success')
    

# view-cart Page   ---------------------

def view_cart(request):
    context = {
        #'all_orders': Order.objects.all(),
        'this_user': User.objects.get(id=request.session['userid'])
        # 'user_orders': User.orders()
    }
    return render (request, 'view-cart.html', context)


#add to Cart -------------------------
def adding_order(request, id4):
    
    product_chosen = Food.objects.get(id=id4)
    quantity = int(request.POST['quantityLabel'])
    price = int(product_chosen.price)
    total_charge = quantity * price
    request.session['entireCharge'] += total_charge
    request.session['entireItems'] += quantity
    
    total_calories = product_chosen.calories * quantity
    request.session['entireCalories'] += total_calories
    # request.session['itemNames'] += product_chosen.name
    
    Order.objects.create(
        quantity = request.POST['quantityLabel'],
        price = total_charge, 
        total_calorie = total_calories,
        user = User.objects.get(id=request.session['userid']),
        food = Food.objects.get(id=id4)

    )

    return redirect('/view-cart')



# delete Cart items -----------------
def destroyOrder(request, id4):
    delete_order = Order.objects.get(id=id4)
    delete_order.delete()

    return redirect('/view-cart')


def viewOrders(request):

    context = {
        'all_orders': Order.objects.all()
    }

    return render(request, 'orders.html', context)