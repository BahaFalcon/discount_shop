from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователь"""
    list_display = ('email', 'username', 'phone_number')
    list_filter = ('location', 'username')# фильтруем по категории и году выхода
    search_fields = ('username', 'phone_number')# поиск по полям названию и имени категории
    save_on_top = True# перенос меню "сохранить" вверх страницы
    save_as = True# панель "сохранить как новый объект"
    list_display_links = ('username', 'email')# ссылка по имени
    readonly_fields = ('get_image', 'password')

    def get_image(self, obj):  # метод вывода изображений постера в поле "фильмы" в админке
        return mark_safe(f'<img src={obj.avatar.url} width="100" height="110"')

    get_image.short_description = 'Аватар'  # название столбца изображения


