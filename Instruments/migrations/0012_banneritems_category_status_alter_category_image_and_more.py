# Generated by Django 4.0.1 on 2022-01-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instruments', '0011_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_name', models.CharField(max_length=60, unique=True)),
                ('image', models.ImageField(upload_to='BannerImages/%Y/%m/%d', verbose_name='image')),
                ('status', models.CharField(choices=[('p', 'published'), ('d', 'draft')], default='p', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('p', 'published'), ('d', 'draft')], default='p', max_length=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='CategoriesPicture/%Y/%m/%d', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='image',
            field=models.ImageField(upload_to='InstrumentsImage/%Y/%m/%d', verbose_name='image'),
        ),
    ]