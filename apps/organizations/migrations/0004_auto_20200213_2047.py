# Generated by Django 2.2 on 2020-02-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20200211_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='couresorg',
            name='students',
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=20, verbose_name='城市名'),
        ),
    ]
