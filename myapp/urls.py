from django.urls import path
from .views import ItemListView, ItemDetailView, item_list, item_detail
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list-cbv'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail-cbv'),
    path('fbv/items/', item_list, name='item-list-fbv'),
    path('fbv/items/<int:pk>/', item_detail, name='item-detail-fbv'),
] + router.urls
