from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователь"""
    list_display = ('id', 'email', 'username', 'phone_number')
    list_filter = ('location', 'username')
    search_fields = ('username', 'phone_number')
    save_on_top = True
    save_as = True
    list_display_links = ('username', 'email')
    readonly_fields = ('get_image', 'password')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="100" height="110"')

    get_image.short_description = 'Аватарка'


