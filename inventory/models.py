from typing import Dict, List

class Item:
    def __init__(self,item_id:int ,name: str, price: float, description: str, quantity: int):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

class Inventory:
	def __init__(self):
		self.items: Dict[str, Item] = {}

	def add_item(self, item: Item) -> None:	
		if item.item_id in self.items:
			self.items[item.item_id].quantity += item.quantity
		else:
			self.items[item.item_id] = item
	def get_item(self, item_id):
		try:
			return self.items[item_id]
		except KeyError:
			raise ValueError(f"No item found with id {item_id}")

	def remove_item(self, item_id: str, quantity: int) -> None:
		if item_id in self.items:
			if self.items[item_id].quantity >= quantity:
				self.items[item_id].quantity -= quantity
				if self.items[item_id].quantity == 0:
					del self.items[item_id]
			else:
				raise ValueError(f"Not enough stock for item with id {item_id}")
		else:
			raise ValueError(f"No item found with id {item_id}")

	def list_items(self) -> List[Item]:
		return list(self.items.values())

	def check_stock(self, item_id: str, quantity: int) -> bool:
		if item_id in self.items:
			return self.items[item_id].quantity >= quantity
		return False

	def reduce_item_quantity(self, item_id: int, quantity: int) -> None:
		if item_id in self.items:
			if self.items[item_id].quantity >= quantity:
				self.items[item_id].quantity -= quantity
			else:
				raise ValueError(f"Not enough stock for item with id {item_id}")
		else:
			raise ValueError(f"No item found with id {item_id}")