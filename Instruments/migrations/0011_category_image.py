# Generated by Django 4.0.1 on 2022-01-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instruments', '0010_alter_instrument_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=0, upload_to='CategoriesPicture/image/%Y/%m/%d', verbose_name='image'),
            preserve_default=False,
        ),
    ]