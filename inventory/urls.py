from django.urls import path
from . import views

urlpatterns = [
	path('items/', views.ItemList.as_view(), name = 'item-list'),
	path('items/add/', views.AddItem.as_view(), name = 'add-item'),
	path('items/<int:item_id>/', views.GetItem.as_view(), name = 'get-item'),
]
