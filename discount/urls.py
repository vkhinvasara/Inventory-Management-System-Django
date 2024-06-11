from django.urls import path
from . import views

urlpatterns = [
    path('create_discount/', views.DiscountView.as_view()),
	path('delete_discount/<int:discount_id>/', views.DiscountView.as_view()),
]