from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from inventory.models import Item, Inventory
from .serializers import CartSerializer, ItemSerializer

class CartView(APIView):
    def get(self, request, customer_id):
        cart = Cart(customer_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request, customer_id):
        item = ItemSerializer(data=request.data)
        if item.is_valid():
            cart = Cart(customer_id)
            cart.add_item(item.validated_data, request.data.get('quantity', 1))
            return Response({'status': 'item added'})
        else:
            return Response(item.errors, status=400)

class CartAddItemView(APIView):
    def post(self, request, customer_id):
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity', 1)
        if item_id is not None:
            try:
                # Get the inventory instance
                inventory = Inventory()
                # Check if the item exists in the inventory
                if item_id in inventory.items:
                    # Get the item from the inventory
                    item = inventory.get_item(item_id)
                    # Get the cart for the customer
                    cart = Cart.objects.get(customer_id=customer_id)
                    # Add the item to the cart
                    cart.add_item(item, quantity)
                    cart.save()
                    return Response({'status': 'item added'})
                else:
                    return Response({'error': 'Item does not exist in inventory'}, status=400)
            except ValueError:
                return Response({'error': 'Inventory does not exist'}, status=400)
        else:
            return Response({'error': 'Invalid item_id'}, status=400)

class CartRemoveItemView(APIView):
    def post(self, request, customer_id):
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity', 1)
        if item_id:
            cart = Cart(customer_id)
            cart.remove_item(item_id, quantity)
            return Response({'status': 'item removed'})
        else:
            return Response({'error': 'Invalid item_id'}, status=400)

class CartTotalView(APIView):
    def get(self, request, customer_id):
        cart = Cart(customer_id)
        total = cart.calculate_total()
        return Response({'total': total})