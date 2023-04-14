from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField
from .models import Category, Store, Topical, Promotion


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'cat_image')


class StoreSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='title', read_only=True)
    logo = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = Store
        fields = (
            'category', 'id', 'logo', 'name', 'value',
            'location', 'work_time', 'description', 'city',
            'phone_number', 'telegram_link', 'vk_link', 'whatsapp_link',
        )


class CategoryStoreSerializer(serializers.ModelSerializer):
    stores = StoreSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'cat_image', 'stores')
