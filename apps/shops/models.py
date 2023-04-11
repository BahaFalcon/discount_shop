from django.db import models
from apps.base.helper import category_img_path, validate_size_image, store_img_path
from django.core.validators import RegexValidator, FileExtensionValidator


class Category(models.Model):
    """Класс для категорий"""
    title = models.CharField('Заголовок', max_length=255)
    cat_image = models.ImageField(
        'Изображение',
        upload_to=category_img_path,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), validate_size_image],
        help_text='Пожалуйста используйте формат JPEG или JPG'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Store(models.Model):
    """Магазин/Организация"""
    CITY_CHOICES = (
        ('Бишкек', 'Бишкек'),
        ('Ош', 'Ош'),
    )
    name = models.CharField('Название', max_length=250)
    logo = models.ImageField(
        'Логотип',
        upload_to=store_img_path,
        validators=[FileExtensionValidator(allowed_extensions=['png'])],
        help_text='Пожалуйста используйте формат PNG'
    )
    phone_regex = RegexValidator(
        regex=r'^\+996 \d{3} \d{2}-\d{2}-\d{2}$',
        message="Номер телефона должен быть в формате: '+996 xxx xx-xx-xx'"
    )
    phone_number = models.CharField('Номер телефона', validators=[phone_regex], max_length=17, unique=True)
    city = models.CharField('Город', max_length=30, choices=CITY_CHOICES)
    location = models.TextField('Адресс:', help_text='Улица, номер дома/строения/корпуса, этаж, номер офиса/кабинета')
    work_time = models.CharField('Время работы:', max_length=250, help_text='Пример: с 10:00 до 20:00')
    value = models.PositiveIntegerField('Скидка', default=0)
    description = models.TextField('Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='stores', verbose_name='Категория')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    whatsapp_link = models.URLField('WhatsApp', null=True, blank=True)
    telegram_link = models.URLField('Telegram', null=True, blank=True)
    vk_link = models.URLField('WhatsApp', null=True, blank=True)

    class Meta:
        verbose_name = 'Магазин/Организация'
        verbose_name_plural = 'Магазины/Организации'

    def __str__(self):
        return self.name

