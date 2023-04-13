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
    list_display = ('id', 'get_image', 'name', 'location', 'phone_number', 'category')
    list_filter = ('category', 'name')
    fields = [
        'name', 'logo', 'preview', 'category', 'phone_number', 'city',
        'location', 'work_time', 'value', 'description', 'whatsapp_link',
        'telegram_link', 'vk_link'
    ]
    search_fields = ('name', 'phone_number')
    save_on_top = True
    save_as = True
    list_display_links = ('name', 'get_image')
    readonly_fields = ('preview',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="60" height="60"')

    def preview(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="430" height="330">')

    get_image.short_description = 'Логотип'


@admin.register(Topical)
class TopicalAdmin(admin.ModelAdmin):
    """Актуальное"""
    list_display = ('id', 'get_image', 'title', 'store')
    list_filter = ('store', 'published')
    search_fields = ('title', 'store')
    save_on_top = True
    save_as = True
    list_display_links = ('get_image', 'title')
    readonly_fields = ('preview',)

    def display_store(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([store.name for store in self.store.all()[:3]])

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.topical_img.url} width="100" height="110"')

    def preview(self, obj):
        return mark_safe(f'<img src={obj.topical_img.url} width="430" height="330">')

    get_image.short_description = 'Изображение Актуальное'
    display_store.short_description = 'Магазин/Организация'


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'get_image', 'title', 'store')
    list_filter = ('store', 'published')
    search_fields = ('title', 'store')
    save_on_top = True
    save_as = True
    list_display_links = ('get_image', 'title')
    readonly_fields = ('preview',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.promotion_img.url} width="100" height="110"')

    def preview(self, obj):
        return mark_safe(f'<img src={obj.promotion_img.url} width="430" height="330">')

    get_image.short_description = 'Изображение Актуальное'


admin.site.site_title = 'DISCOUNT'
admin.site.site_header = 'DISCOUNT'
