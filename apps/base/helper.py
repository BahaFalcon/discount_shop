from django.core.exceptions import ValidationError


def user_avatar_path(instance, filename):
    # Функция генерирует путь к папке для сохранения изображения пользователя
    # Путь будет иметь вид: "avatars/user.username/<filename>"
    return f"avatars/{instance.username}/{filename}"

def category_img_path(instance, filename):
    # Функция генерирует путь к папке для сохранения изображения категорий
    # Путь будет иметь вид: "category/title/<filename>"
    return f"category/{instance.title}/{filename}"

def store_img_path(instance, filename):
    # Функция генерирует путь к папке для сохранения изображения магазина
    # Путь будет иметь вид: "store/name/<filename>"
    return f"store/{instance.name}/{filename}"

# def user_directory_path(instance, filename):
#     # Функция генерирует путь к папке для сохранения изображения пользователя
#     # Путь будет иметь вид: "avatars/user_<id>/<filename>"
#     ext = os.path.splitext(filename)[1].lower()
#     if ext in ['.jpg', '.jpeg']:
#         return f"avatars/user_{instance.id}/{filename}"
#     else:
#         raise ValueError('Недопустимый формат файла')


def validate_size_image(file_obj):
    """Проверка размера файла"""
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError('Максимальный размер файла %(limit_value)s MB', params={'limit_value': megabyte_limit})
