from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from order_module.models import Order,OrderItem
from product.models import Product


# Create your views here.
def add_to_cart(request: HttpRequest):
    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity')

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, isActive=True).first()
        if product is not None:

            # current_order = Order.objects.filter(user_id=request.user.id, isPaid=False).first()
            current_order, created = Order.objects.get_or_create(isPaid=False, user_id=request.user.id)
            COrder:Order = current_order
            currentOrderItems: OrderItem = COrder.orders.filter(product_id=product_id).first()
            if currentOrderItems is not None:
                currentOrderItems.quantity +=int(quantity)
                currentOrderItems.save()
            else:
                newOrderItem = OrderItem(order_id=current_order.id, product_id=product_id, quantity=quantity)
                newOrderItem.save()

            return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({
            'status': 'Not authenticated'
        })
