from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

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

    class Meta:
        verbose_name = 'Գործընկեր'
        verbose_name_plural = 'Գործընկերներ'


class BannerItems(models.Model):
    Image_name = models.CharField(max_length=60, unique=True)
    image = models.ImageField('image', upload_to='BannerImages/%Y/%m/%d', )
    status = models.CharField(max_length=1, choices=satus_choice, default='p')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Image_name

    class Meta:
        verbose_name = 'Բանների լուսանկար'
        verbose_name_plural = 'Բանների լուսանկարներ'


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField('image', upload_to='CategoriesPicture/%Y/%m/%d', )
    status = models.CharField(max_length=1, choices=satus_choice, default='p')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Բաժին'
        verbose_name_plural = 'Բաժիններ'


class InstrumentContent(models.Model):
    header = models.CharField(max_length=200, verbose_name='Header', blank=True, null=True)
    full_description = RichTextField(verbose_name='Full description')
    image = models.ImageField(upload_to='InstrumentsImage/%Y/%m/%d', verbose_name='Pictures')

    def __str__(self):
        if self.header is not None:
            return self.header
        else:
            return 'No Header'
    class Meta:
        verbose_name = 'Սարքավորուման կոնտենտ'
        verbose_name_plural = 'Սարքավորումների կոնտենտներ'
        

class ModelContent(models.Model):
    header = models.CharField(max_length=200, verbose_name='Header', blank=True, null=True)
    full_description = RichTextField(verbose_name='Full description')
    image = models.ImageField(upload_to='ModelImage/%Y/%m/%d', verbose_name='Pictures')

    def __str__(self):
        if self.header is not None:
            return self.header
        else:
            return 'No Header'

    class Meta:
        verbose_name = 'Մոդել կոնտենտ'
        verbose_name_plural = 'Մոդել կոնտենտներ'


class InstrumentModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ModelImage/%Y/%m/%d', verbose_name='Pictures')
    short_description = RichTextField(max_length=500, verbose_name='Short description')
    big_image = models.ImageField(upload_to='ModelImage/%Y/%m/%d', verbose_name='Header image ')
    model_content = models.ManyToManyField(ModelContent)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Սարքավորման մոդել'
        verbose_name_plural = 'Սարքավորման մոդեներ'

class Instrument(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Instrument Name')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    image = models.ImageField(upload_to='InstrumentsImage/%Y/%m/%d')
    short_description = RichTextField(max_length=500, verbose_name='First Short description')
    short_description2 = RichTextField(max_length=2000, verbose_name='Second Short description')
    instrument_category = models.ManyToManyField(Category, verbose_name='Main Category', related_name='Category')
    instrument_Content = models.ManyToManyField(InstrumentContent, verbose_name='InstrumentContent',
                                                related_name='InstrumentContent')
    instrument_model = models.ManyToManyField(InstrumentModel,
                                              verbose_name='Instrument Model',
                                              related_name='Instrument_Model')
    video = models.FileField(upload_to='InstrumentsVideos/%Y/%m/%d', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])],
                             verbose_name='Video')
    status = models.CharField(max_length=1, choices=satus_choice, default='p')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Սարքավորում'
        verbose_name_plural = 'Սարքավորումներ'