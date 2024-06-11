from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from inventory.views import inventory
from discount.views import discount_manager

carts = {}
class CartView(APIView):
    def get(self, request, customer_id):
        if customer_id in carts:
            cart = carts[customer_id]
            items = cart.get_items().values()
            # manually create the response data
            response_data = {
                'customer_id': cart.customer_id,
                'items': [{ 'item_id': item.item_id, 'name': item.name, 'quantity': item.quantity } for item in items],
                'total': cart.calculate_total()
            }
            return Response(response_data)
        else:
            return Response({'error': 'Cart does not exist'}, status=400)
class CartAddItemView(APIView):
	def post(self, request, customer_id):
		item_id = request.data.get('item_id')
		quantity = request.data.get('quantity', 1)
  
		if item_id is not None:
			try:
				if item_id in inventory.items:
					if customer_id not in carts:
						carts[customer_id] = Cart(customer_id, inventory)         
					cart = carts[customer_id]
					item = inventory.get_item(item_id)
					cart.add_item(item.item_id, quantity)
					carts[customer_id] = cart
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

class CartApplyDiscountView(APIView):
     def get(self, request, customer_id, discount_id):
        cart = carts[customer_id]
        total = cart.calculate_total()

        total_after_discount = discount_manager.apply_discount(total, discount_id)

        return Response({'total_after_discount': total_after_discount})