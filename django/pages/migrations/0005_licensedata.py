# Generated by Django 3.0.8 on 2021-01-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201228_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseData',
            fields=[
                ('license_auto_id', models.AutoField(primary_key=True, serialize=False, verbose_name='License ID')),
                ('license_auto_date', models.DateTimeField(auto_now=True, verbose_name='Kayıt Tarihi ve Saati')),
                ('license_code', models.CharField(max_length=50, verbose_name='Code')),
                ('license_icon', models.CharField(max_length=1000, verbose_name='Icon')),
                ('license_deed', models.CharField(max_length=500, verbose_name='URL')),
                ('license_info', models.CharField(max_length=500, verbose_name='Info')),
            ],
        ),
    ]
