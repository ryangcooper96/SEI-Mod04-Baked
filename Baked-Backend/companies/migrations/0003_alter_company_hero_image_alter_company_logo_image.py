# Generated by Django 4.1.3 on 2022-11-25 10:47

import companies.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_rename_user_id_company_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='hero_image',
            field=models.ImageField(blank=True, null=True, upload_to=companies.models.upload_to),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to=companies.models.upload_to),
        ),
    ]
