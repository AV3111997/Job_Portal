from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cart, CartItem, Product

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    subtotal = sum(item.product.price * item.quantity for item in items)
    shipping = 10 if subtotal > 0 else 0  # Flat rate shipping
    total = subtotal + shipping
    return render(request, 'cart.html', {
        'items': items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('view_cart')

@login_required
def update_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        item.quantity = quantity
        item.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
