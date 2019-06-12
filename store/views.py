from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def catalog(request):

    products = Product.objects.all()

    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']
    request.session.set_expiry(0)

    ctx = {
        'products': products,
        'cart_items_count': len(cart)
    }

    if request.method == "POST":
        cart.append(request.POST.get('product_id'))
        return redirect('catalog')


    return render(request, 'catalog.html', ctx)

def cart_items(cart):
    items = []
    for item in cart:
        items.append(Product.objects.get(id=int(item)))
    return items

def total_price(cart_items):
    total = 0;
    for cart_item in cart_items:
        total += cart_item.price
    return total


def cart(request):

    cart = request.session['cart']
    items = cart_items(cart)

    ctx = {
        "cart_items": items,
        "cart_items_count": len(cart),
        "total_price":total_price(items)
    }

    return render(request, 'cart.html', ctx)


def removeItemFromCart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)

    if request.POST:
        item_id = request.POST.get('obj_id')
        index = cart.index(item_id)
        cart.pop(index)

    return redirect('cart')


def checkout(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    items = cart_items(cart)

    ctx = {
        "cart_items": items,
        "cart_items_count": len(cart),
        "total_price": total_price(items)
    }

    return render(request, "checkout.html", ctx)


def submitOrder(request):

    new_order = Order()
    cart = request.session['cart']

    if request.POST:
        new_order.first_name = request.POST.get('first')
        new_order.last_name = request.POST.get('last')
        new_order.address = request.POST.get('address')
        new_order.city = request.POST.get('city')
        new_order.payment_method = request.POST.get('paymentMethod')
        new_order.payment_data = request.POST.get('paymentData')
        new_order.fulfilled = False

        for cart_item in cart:
            item = Product.objects.get(id=int(cart_item))
            new_order.items += item.name + " - " + str(item.price) + " - " + item.description + "; "

        new_order.save()

    request.session['cart'] = []

    return render(request, 'complete.html', None)


def admin_login(request):
    if request.POST:
        un = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request,username=un,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('admin')

        else:
            return render(request,'admin_login.html', {'login_error': 'Unable to login'})

    return render(request, 'admin_login.html', None)


@login_required(login_url='/catalog/admin-login')
def admin_dashboard(request):

    orders = Order.objects.all()
    ctx = {'orders': orders}

    return render(request, 'admin_dashboard.html', ctx)
