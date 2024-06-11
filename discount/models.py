
class Discount:
    def __init__(self, discount_id, discount_percentage, maximum_discount_cap):
        self.discount_id = discount_id
        self.discount_percentage = discount_percentage
        self.maximum_discount_cap = maximum_discount_cap
        
class DiscountManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DiscountManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.discounts = {}

    def add_discount(self, discount_id, discount_percentage, maximum_discount_cap):
        self.discounts[discount_id] = Discount(discount_id, discount_percentage, maximum_discount_cap)

    def remove_discount(self, discount_id):
        if discount_id in self.discounts:
            del self.discounts[discount_id]

    def apply_discount(self, cart_value, discount_id):
        if discount_id in self.discounts:
            discount = self.discounts[discount_id]
            discount_value = min(cart_value * (discount.discount_percentage / 100), discount.maximum_discount_cap)
            return cart_value - discount_value
        else:
            raise ValueError(f"No discount found with id {discount_id}")
