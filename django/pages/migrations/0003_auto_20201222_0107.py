# Generated by Django 3.0.8 on 2020-12-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201222_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oerdata',
            name='oer_auto_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Kayıt Tarihi ve Saati'),
        ),
    ]
