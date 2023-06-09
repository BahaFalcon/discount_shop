# Generated by Django 3.2 on 2023-03-30 05:08

import apps.base.helper
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Эл.почта')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('username', models.CharField(max_length=60, unique=True, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(max_length=60, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=60, verbose_name='Отчество')),
                ('avatar', models.ImageField(blank=True, help_text='Пожалуйста используйте формат JPEG или JPG', null=True, upload_to=apps.base.helper.user_avatar_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), apps.base.helper.validate_size_image], verbose_name='Аватар')),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+996 xxx xx-xx-xx'", regex='^\\+996 \\d{3} \\d{2}-\\d{2}-\\d{2}$')], verbose_name='Номер телефона')),
                ('location', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош')], max_length=30, verbose_name='Город')),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], default='М', max_length=20, verbose_name='Пол')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('reset_password_code', models.IntegerField(verbose_name='Koд для сброса пароля')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
