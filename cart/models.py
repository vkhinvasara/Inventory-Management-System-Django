from typing import Dict
from inventory.models import Item, Inventory
class Cart:
	def __init__(self, customer_id: str, inventory: Inventory):
		self.customer_id = customer_id
		self.items: Dict[str, Item] = {}
		self.inventory = inventory

	def add_item(self, item_id: int, quantity: int = 1) -> None:
		if self.inventory.check_stock(item_id, quantity):
			item = self.inventory.items[item_id]
			if item.item_id in self.items:
				self.items[item.item_id].quantity += quantity
			else:
				self.items[item_id] = item
				self.items[item.item_id].quantity = quantity
		else:
			raise ValueError(f"No item found with id {item_id} or not enough stock")

	def remove_item(self, item_id: str, quantity: int) -> None:
		if item_id in self.items:
			self.items[item_id].quantity -= quantity
			if self.items[item_id].quantity <= 0:
				del self.items[item_id]

	def calculate_total(self) -> float:
		return sum([item.price * item.quantity for item in self.items.values()])
