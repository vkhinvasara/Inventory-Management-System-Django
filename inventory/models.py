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

	def add_product(self, item: Item) -> None:	
		if item.item_id in self.items:
			self.items[item.item_id].quantity += item.quantity
		else:
			self.items[item.item_id] = item

	def remove_product(self, item_name: str) -> None:
		if item_name in self.products:
			del self.products[item_name]

	def list_products(self) -> List[Item]:
		return list(self.items.values())