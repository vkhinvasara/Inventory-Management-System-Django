# Inventory Management System

This is an API for an Inventory Management System built with Django. The API is hosted at [nutmaster101.pythonanywhere.com](http://nutmaster101.pythonanywhere.com).

## API Endpoints

The following endpoints are available:

- `GET /<int:customer_id>/`: Retrieve the cart for a specific customer.
- `POST /<int:customer_id>/add/`: Add an item to a specific customer's cart.
- `POST /<int:customer_id>/remove/`: Remove an item from a specific customer's cart.
- `GET /<int:customer_id>/total/`: Get the total cost of items in a specific customer's cart.
- `POST /<int:customer_id>/discount/<str:discount_id>/`: Apply a discount to a specific customer's cart.
- `POST /<int:customer_id>/checkout/`: Checkout a specific customer's cart.

Please replace `<int:customer_id>` with the actual customer ID and `<str:discount_id>` with the actual discount ID.

## Postman Collection

The Postman collection for this API is available [here](https://api.postman.com/collections/17145261-7dcb8e9a-dc54-4508-9e5f-b1af49aceb47?access_key=PMAT-01J0582DY79YHW64YGEQKNGTGW).

## Local Development

To set up this project for local development:

1. Clone this repository.
2. Install the dependencies listed in the [requirements.txt](requirements.txt) file.
3. Run the Django server with `python manage.py runserver`.

## Testing

To run the tests, use the command `python manage.py test`.

## Deployment

This API is currently deployed on [PythonAnywhere](http://nutmaster101.pythonanywhere.com).

## Features

1. **Inventory Stock Check**: The system checks if an item is available in the inventory and if there is enough stock before adding it to the cart.
2. **Item Quantity Management**: The system allows for the quantity of an item to be specified when adding to the cart. If the item is already in the cart, the quantity is increased.
3. **Cart Total Calculation**: The system calculates the total cost of the items in the cart.
4. **Discount Application**: The system allows for a discount coupon to be applied to the cart.
5. **Cart Emptying**: The system allows for the cart to be emptied.
6. **Discount Cap**: The system ensures that the discount applied does not exceed the maximum discount cap specified in the discount coupon.
7. **Item Removal**: The system allows for an item to be removed from the cart. If the quantity specified is more than the quantity in the cart, the item is removed completely.
8. **Inventory Management**: The system allows for items to be added and removed from the inventory.
9. **Discount Management**: The system allows for discounts to be added and removed.
10. **Error Handling**: The system raises appropriate errors when an operation cannot be performed, such as when trying to add an item that is not in the inventory to the cart, or when trying to apply a discount that does not exist.
