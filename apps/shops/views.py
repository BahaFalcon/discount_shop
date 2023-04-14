from django.shortcuts import render
from .models import Category, Store, Topical, Promotion
from .serializers import CategorySerializer, StoreSerializer, CategoryStoreSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CategoryListAPIView(ListAPIView):
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


class CategoryStoreView(generics.ListAPIView):
    """Получить организации по категориям"""
    queryset = Category.objects.all()
    serializer_class = CategoryStoreSerializer

    @swagger_auto_schema(
        operation_summary='Получить организации по категориям',
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

