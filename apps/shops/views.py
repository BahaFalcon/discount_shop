from django.shortcuts import render
from .models import Category, Store, Topical, Promotion
from .serializers import (
    CategorySerializer, StoreSerializer, CategoryStoreSerializer,
    TopicalListSerializer, TopicalSerializer, PromotionListSerializer,
    PromotionSerializer
)
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CategoryListAPIView(ListAPIView):
    """Получить все категории"""
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class StoreListView(generics.ListAPIView):
    """Получить все организации"""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    @swagger_auto_schema(
        operation_summary='Получить все Магазины/Организации',
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': StoreSerializer(many=True)},
    )
    def get(self, request):
        store = Store.objects.all()
        serializers = StoreSerializer(store, many=True)
        data = serializers.data
        for obj in data:
            obj['logo'] = request.build_absolute_uri(obj['logo'])
        return Response(data, status=status.HTTP_200_OK)


class StoreDetailView(APIView):
    """Получить одну организацию"""

    @swagger_auto_schema(
        operation_summary='Получить один Магазин/Организацию',
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': StoreSerializer(many=True)},
    )
    def get(self, request, pk):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(store)
        data = serializer.data
        data['logo'] = request.build_absolute_uri(data['logo'])

        return Response(data)


class CategoryStoreListView(generics.ListAPIView):
    """Получить список категорий с организациями"""
    queryset = Category.objects.all()
    serializer_class = CategoryStoreSerializer

    @swagger_auto_schema(
        operation_summary='Получить список категорий с организациями',
        operation_description='Берем из базы все записи отсортированный по айдишке',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': CategoryStoreSerializer(many=True)},
    )
    def get(self, request):
        title_qp = self.request.query_params.get('title')
        if title_qp:
            category_qs = Category.objects.filter(title__icontains=title_qp)
        else:
            category_qs = Category.objects.all()
        srz = CategoryStoreSerializer(category_qs, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)


class CategoryStoreView(APIView):
    """Получить одну категорию с организациями"""

    @swagger_auto_schema(
        operation_summary='Получить одну категорию с организациями',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': CategoryStoreSerializer(many=True)},
    )
    def get(self, request, pk):
        category_qs = Category.objects.filter(pk=pk)
        srz = CategoryStoreSerializer(category_qs, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)


class TopicalListView(generics.ListAPIView):
    """Получить все запаси Актуальное"""
    queryset = Topical.objects.all()
    serializer_class = TopicalListSerializer

    @swagger_auto_schema(
        operation_summary='Получить все запаси Актуальное',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': TopicalListSerializer(many=True)},
    )
    def get(self, request):
        store = Topical.objects.all()
        serializers = TopicalListSerializer(store, many=True)
        data = serializers.data
        for obj in data:
            obj['topical_img'] = request.build_absolute_uri(obj['topical_img'])
        return Response(data, status=status.HTTP_200_OK)


class TopicalDetailView(APIView):
    """Получить одну запись Актуальное"""

    @swagger_auto_schema(
        operation_summary='Получить одну запись Актуальное',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': TopicalSerializer(many=True)},
    )
    def get(self, request, pk):
        try:
            topical = Topical.objects.get(pk=pk)
        except Topical.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TopicalSerializer(topical)
        data = serializer.data
        data['topical_img'] = request.build_absolute_uri(data['topical_img'])

        return Response(data)


class PromotionListView(generics.ListAPIView):
    """Получить все запаси Акции"""
    queryset = Promotion.objects.all()
    serializer_class = PromotionListSerializer

    @swagger_auto_schema(
        operation_summary='Получить все запаси Акции',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': PromotionListSerializer(many=True)},
    )
    def get(self, request):
        promo = Promotion.objects.all()
        serializers = PromotionListSerializer(promo, many=True)
        data = serializers.data
        for obj in data:
            obj['promotion_img'] = request.build_absolute_uri(obj['promotion_img'])
        return Response(data, status=status.HTTP_200_OK)


class PromotionDetailView(APIView):
    """Получить одну запись Акция"""

    @swagger_auto_schema(
        operation_summary='Получить одну запись Акция',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': PromotionSerializer(many=True)},
    )
    def get(self, request, pk):
        try:
            promo = Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PromotionSerializer(promo)
        data = serializer.data
        data['promotion_img'] = request.build_absolute_uri(data['promotion_img'])

        return Response(data)


