from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.core.validators import RegexValidator, FileExtensionValidator
from apps.base.helper import user_avatar_path, validate_size_image


class User(AbstractBaseUser):
    """Пользователь"""

    GENDER_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )
    LOCATION_CHOICES = (
        ('Бишкек', 'Бишкек'),
        ('Ош', 'Ош'),
    )
    email = models.EmailField('Эл.почта', max_length=100, blank=True, null=True, unique=True)
    password = models.CharField('Пароль', max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField('Имя пользователя', max_length=60, unique=True)
    first_name = models.CharField('Имя', max_length=60)
    last_name = models.CharField('Фамилия', max_length=60)
    patronymic = models.CharField('Отчество', max_length=60)
    avatar = models.ImageField(
        'Аватар',
        upload_to=user_avatar_path,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), validate_size_image],
        help_text='Пожалуйста используйте формат JPEG или JPG'
    )
    phone_regex = RegexValidator(
        regex=r'^\+996 \d{3} \d{2}-\d{2}-\d{2}$',
        message="Номер телефона должен быть в формате: '+996 xxx xx-xx-xx'"
    )
    phone_number = models.CharField('Номер телефона', validators=[phone_regex], max_length=17, unique=True)
    location = models.CharField('Город', max_length=30, choices=LOCATION_CHOICES)
    gender = models.CharField('Пол', max_length=20, choices=GENDER_CHOICES, default='М')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    birth_date = models.DateField('Дата рождения', null=True)
    reset_password_code = models.IntegerField('Koд для сброса пароля', null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username + "," + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

