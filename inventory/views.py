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
        items = [item.__dict__ for item in inventory.list_items()]
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
		inventory.add_item(item)
		return Response(item.__dict__, status=status.HTTP_201_CREATED)

class GetItem(APIView):
	"""
	Get a product from the inventory.
	"""
	def get(self, request, item_id, format = None):
		try:
			item = inventory.get_item(item_id)
			return Response(item.__dict__)
		except ValueError as e:
			return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class DeleteItem(APIView):
	"""
	Delete a product from the inventory.
	"""
	def delete(self, request, item_id, quantity, format = None):
		try:
			inventory.remove_item(item_id, quantity)
			return Response({'message': 'Item deleted successfully'})
		except ValueError as e:
			return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)