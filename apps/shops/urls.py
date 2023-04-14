from django.urls import path
from .views import CategoryListAPIView, StoreListView, StoreDetailView,  CategoryStoreView

app_name = 'shops'

urlpatterns = [
    path('api/v1/category_list/', CategoryListAPIView.as_view(), name='all-categories'),
    path('api/v1/store_list/', StoreListView.as_view(), name='all-stores'),
    path('api/v1/store_detail/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('api/v1/categories_with_stores/',  CategoryStoreView.as_view(), name='cat-with-stores'),
]
