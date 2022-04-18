from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

satus_choice = (
    ('p', 'published'),
    ('d', 'draft'),
)


class Partner(models.Model):
    name = models.CharField(max_length=60, unique=True)
    image = models.ImageField('image', upload_to='Partners/%Y/%m/%d', )
    status = models.CharField(max_length=1, choices=satus_choice, default='p')

    def __str__(self):
        return self.name


class BannerItems(models.Model):
    Image_name = models.CharField(max_length=60, unique=True)
    image = models.ImageField('image', upload_to='BannerImages/%Y/%m/%d', )
    status = models.CharField(max_length=1, choices=satus_choice, default='p')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Image_name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField('image', upload_to='CategoriesPicture/%Y/%m/%d', )
    status = models.CharField(max_length=1, choices=satus_choice, default='p')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    short_description = RichTextUploadingField(max_length=500)
    full_description1 = RichTextUploadingField()
    full_description2 = RichTextUploadingField()
    instrument_category = models.ManyToManyField(Category,  verbose_name='Main Category', related_name='Category')
    image = models.ImageField(upload_to='InstrumentsImage/%Y/%m/%d', verbose_name='Picture for All View')
    image2 = models.ImageField(upload_to='InstrumentsImage/%Y/%m/%d', verbose_name='Picture 1 for Detail View')
    image3 = models.ImageField(upload_to='InstrumentsImage/%Y/%m/%d', verbose_name='Picture 2 for Detail View')
    video = models.FileField(upload_to='InstrumentsVideos/%Y/%m/%d', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    status = models.CharField(max_length=1, choices=satus_choice, default='p')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


