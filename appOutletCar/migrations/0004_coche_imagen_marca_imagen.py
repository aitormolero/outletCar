# Generated by Django 5.1.2 on 2024-11-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutletCar', '0003_coche_descapotable'),
    ]

    operations = [
        migrations.AddField(
            model_name='coche',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='marca',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
    ]