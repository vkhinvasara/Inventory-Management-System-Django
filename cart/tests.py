from django.test import TestCase
from .models import Cart
from inventory.models import Item
from inventory.views import inventory
from discount.views import discount_manager
# Create your tests here.

class CartTestCase(TestCase):
	def setUp(self):
		# Create an inventory
		# Add items to the inventory
		item1 = Item(item_id='1', name='Item 1', price=700.0, description='This is item 1', quantity=100)
		item2 = Item(item_id='2', name='Item 2', price=2000.0, description='This is item 2', quantity=50)
		inventory.add_item(item1)
		inventory.add_item(item2)
		# Create a cart for a customer
		self.cart = Cart(customer_id=1, inventory=inventory)
		# Add items to the cart
		self.cart.add_item(item_id='1', quantity=5)
		self.cart.add_item(item_id='2', quantity=2)
		# Add a discount coupon
		discount_manager.add_discount(discount_id='DISCOUNT10', discount_percentage=10, maximum_discount_cap=300)

	def test_cart_total(self):
		# Calculate the total cost
		total = self.cart.calculate_total()
		self.assertEqual(total, 7500.0)

	def test_cart_discount(self):
		# Apply a discount
		self.cart.apply_discount(discount_id='DISCOUNT10')
		self.assertEqual(self.cart.total, 7200.0)

	def test_cart_remove_item(self):
		# Remove an item from the cart
		self.cart.remove_item(item_id='1', quantity=1)
		items = self.cart.get_items()
		self.assertEqual(items['1'].quantity, 4)

	def test_cart_empty(self):
		# Empty the cart
		self.cart.empty_cart()
		items = self.cart.get_items()
		self.assertEqual(len(items), 0)