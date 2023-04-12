from django.contrib import admin
from .models import Category, Store, Topical, Promotion
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('cat_image', 'title',)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Магазин/Организация"""
    list_display = ('id', 'logo', 'name', 'phone_number')
    list_filter = ('location', 'name')
    search_fields = ('name', 'phone_number')
    save_on_top = True
    save_as = True
    list_display_links = ('name', 'logo')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="100" height="110"')

    get_image.short_description = 'Логотип'


@admin.register(Topical)
class TopicalAdmin(admin.ModelAdmin):
    """Актуальное"""
    list_display = ('id', 'topical_img', 'title', 'store')
    list_filter = ('store', 'published')
    search_fields = ('name', 'store')
    save_on_top = True
    save_as = True
    list_display_links = ('topical_img', 'title')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.topical_img.url} width="100" height="110"')

    get_image.short_description = 'Изображение Актуальное'


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'promotion_img', 'title', 'store')
    list_filter = ('store', 'published')
    search_fields = ('name', 'store')
    save_on_top = True
    save_as = True
    list_display_links = ('topical_img', 'title')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.topical_img.url} width="100" height="110"')

    get_image.short_description = 'Изображение Актуальное'

admin.site.site_title = 'DISCOUNT'
admin.site.site_header = 'DISCOUNT'
