# Generated by Django 3.0.5 on 2020-06-10 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200601_1045'),
        ('chart', '0002_auto_20200601_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='sheet_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu', verbose_name='시트 이름'),
        ),
    ]
