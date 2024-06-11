from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory, Item

# Create an instance of the Inventory class.
inventory = Inventory()

class ItemList(APIView):
    """
    List all products in the inventory.
    """
    def get(self, request, format = None):
        items = [item.__dict__ for item in inventory.list_products()]
        return Response(items)

class AddItem(APIView):
	"""
	Add a product to the inventory.
	"""
	def post(self, request, format = None):
		item = Item(
			item_id = request.data.get('item_id'),
			name = request.data.get('name'),
			price = request.data.get('price'),
			description = request.data.get('description'),
			quantity = request.data.get('quantity')
		)
		inventory.add_product(item)
		return Response(item.__dict__, status=status.HTTP_201_CREATED)