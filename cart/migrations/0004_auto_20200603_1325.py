# Generated by Django 3.0.5 on 2020-06-03 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_cart_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]