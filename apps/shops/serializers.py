from rest_framework import serializers
import locale
from rest_framework.serializers import SlugRelatedField
from .models import Category, Store, Topical, Promotion

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'cat_image')


class StoreSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='title', read_only=True)

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


class TopicalListSerializer(serializers.ModelSerializer):
    store = SlugRelatedField(slug_field='name', read_only=True)
    begin = serializers.DateField(format="%d %B")
    end = serializers.DateField(format="%d %B")

    class Meta:
        model = Topical
        fields = ('title', 'topical_img', 'begin', 'end', 'store')


class TopicalSerializer(serializers.ModelSerializer):
    store = SlugRelatedField(slug_field='name', read_only=True)
    begin = serializers.DateField(format="%d %B")
    end = serializers.DateField(format="%d %B")
    published = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Topical
        fields = (
            'title', 'topical_img', 'begin', 'end',
            'published', 'sub_title', 'description',
            'value', 'store'
        )


class PromotionListSerializer(serializers.ModelSerializer):
    store = SlugRelatedField(slug_field='name', read_only=True)
    begin = serializers.DateField(format="%d %B")
    end = serializers.DateField(format="%d %B")

    class Meta:
        model = Promotion
        fields = ('title', 'promotion_img', 'begin', 'end', 'store')


class PromotionSerializer(serializers.ModelSerializer):
    store = SlugRelatedField(slug_field='name', read_only=True)
    begin = serializers.DateField(format="%d %B")
    end = serializers.DateField(format="%d %B")
    published = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Promotion
        fields = (
            'title', 'promotion_img', 'begin', 'end',
            'published', 'sub_title', 'description', 'store'
        )



