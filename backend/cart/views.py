from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from products.models import Product

@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    product = Product.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += int(quantity)
    else:
        cart_item.quantity = int(quantity)

    cart_item.save()

    return Response({"message": "Added to cart"})

# ✅ GET CART ITEMS
@api_view(['GET'])
def get_cart(request):
    cart_items = CartItem.objects.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)

# ✅ UPDATE CART (increase / decrease)
@api_view(['POST'])
def update_cart(request):
    product_id = request.data.get('product_id')
    action = request.data.get('action')

    try:
        cart_item = CartItem.objects.get(product_id=product_id)

        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease":
            cart_item.quantity -= 1
            if cart_item.quantity <= 0:
                cart_item.delete()
                return Response({"message": "Item removed"})

        cart_item.save()
        return Response({"message": "Cart updated"})
    
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

# ✅ REMOVE ITEM COMPLETELY
@api_view(['POST'])
def remove_from_cart(request):
    product_id = request.data.get('product_id')

    try:
        cart_item = CartItem.objects.get(product_id=product_id)
        cart_item.delete()
        return Response({"message": "Item removed"})
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)
    
