from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from order_module.models import Order,OrderItem
from product.models import Product


# Create your views here.
def add_to_cart(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    quantity = int(request.GET.get('quantity'))
    if quantity < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'quantity is not valid',
            'confirm_button_text': 'OK',
            'icon': 'error'
        })
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, isActive=True).first()
        if product is not None:

            # current_order = Order.objects.filter(user_id=request.user.id, isPaid=False).first()
            current_order, created = Order.objects.get_or_create(isPaid=False, user_id=request.user.id)
            COrder: Order = current_order
            currentOrderItems: OrderItem = COrder.orders.filter(product_id=product_id).first()
            if currentOrderItems is not None:
                currentOrderItems.quantity += quantity
                currentOrderItems.save()
            else:
                newOrderItem = OrderItem(order_id=current_order.id, product_id=product_id, quantity=quantity)
                newOrderItem.save()

            return JsonResponse({
                'status': 'success',
                'text': 'Added to cart',
                'confirm_button_text': 'Thanks',
                'icon': 'success'
            })
    else:
        return JsonResponse({
            'status': 'Not_authenticated',
            'text': 'Please Login first',
            'confirm_button_text': 'Lets go',
            'icon': 'warning'

        })
