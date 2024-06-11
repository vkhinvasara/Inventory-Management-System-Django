from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DiscountManager

discount_manager = DiscountManager()  
class DiscountView(APIView):
    def post(self, request):
        discount_id = request.data.get('discount_id')
        discount_percentage = request.data.get('discount_percentage')
        maximum_discount_cap = request.data.get('maximum_discount_cap')

        if not all([discount_id, discount_percentage, maximum_discount_cap]):
            return Response({'error': 'Missing required parameters'}, status=400)

        discount_manager.add_discount(discount_id, discount_percentage, maximum_discount_cap)

        return Response({'message': 'Discount added successfully'})

    def delete(self, request, discount_id):
        discount_manager.remove_discount(discount_id)

        return Response({'message': 'Discount removed successfully'})