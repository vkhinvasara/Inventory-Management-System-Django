from django.urls import path
from . import views

urlpatterns = [
    path('<int:customer_id>/', views.CartView.as_view()),
    path('<int:customer_id>/add/', views.CartAddItemView.as_view()),
	path('<int:customer_id>/remove/', views.CartRemoveItemView.as_view()),
	path('<int:customer_id>/total/', views.CartTotalView.as_view()),
	path('<int:customer_id>/discount/<str:discount_id>/', views.CartApplyDiscountView.as_view()),
	path('<int:customer_id>/checkout/', views.CheckoutView.as_view()),
]