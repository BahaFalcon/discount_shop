# Generated by Django 3.2 on 2023-03-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reset_password_code',
            field=models.IntegerField(null=True, verbose_name='Koд для сброса пароля'),
        ),
    ]
