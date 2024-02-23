# urls.py

from django.urls import path
from .views import add_inventory, change_inventory,  pending_inventory, approve_inventory_item
from myinventory import views
urlpatterns = [
    path('inventory/add/', add_inventory),
    path('inventory/<int:item_id>/change/', change_inventory),
    path('inventory/<int:item_id>/remove/',views.remove_inventory, name = 'remove_inventory'),
    path('inventory/pending/', pending_inventory),
    path('inventory/<int:item_id>/approve/', views.approve_inventory_item,name ='approve_inventory_item'),
]
