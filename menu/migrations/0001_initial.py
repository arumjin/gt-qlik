# Generated by Django 3.0.5 on 2020-05-22 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_rank', models.CharField(blank=True, max_length=20, verbose_name='우선순위')),
                ('title', models.CharField(max_length=128, verbose_name='메뉴 이름')),
                ('url', models.TextField(verbose_name='URL')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '화면설정 메뉴',
                'verbose_name_plural': '화면설정 메뉴',
                'db_table': '화면설정 메뉴',
            },
        ),
    ]