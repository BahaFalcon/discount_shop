from django.urls import path
from .views import (
    CategoryListAPIView, StoreListView, StoreDetailView,
    CategoryStoreListView, CategoryStoreView, TopicalListView,
    TopicalDetailView, PromotionListView, PromotionDetailView
)

app_name = 'shops'

urlpatterns = [
    path('api/v1/category_list/', CategoryListAPIView.as_view(), name='all-categories'),
    path('api/v1/store_list/', StoreListView.as_view(), name='all-stores'),
    path('api/v1/store_detail/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('api/v1/categories_with_stores/',  CategoryStoreListView.as_view(), name='cat-with-stores-list'),
    path('api/v1/categories_with_stores/<int:pk>/',  CategoryStoreView.as_view(), name='cat-with-store'),
    path('api/v1/topical_list/', TopicalListView.as_view(), name='topical-list'),
    path('api/v1/topical_detail/<int:pk>/', TopicalDetailView.as_view(), name='topical-detail'),
    path('api/v1/promotion_list/', PromotionListView.as_view(), name='promo-list'),
    path('api/v1/promotion_detail/<int:pk>/', PromotionDetailView.as_view(), name='promo-detail'),
]
