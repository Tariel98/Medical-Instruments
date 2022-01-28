from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.


def make_published(self, request, queryset):
    queryset.update(status='p')
    self.message_user(request, "successfully marked as published.")


def make_draft(self, request, queryset):
    queryset.update(status='d')
    self.message_user(request, "successfully marked as draft.")


make_published.short_description = "Mark selected Instruments as published"
make_draft.short_description = "Mark selected Instruments as draft"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('status',)
    actions = [make_published, make_draft]
    readonly_fields = ['date']
    list_display = ('name', 'status', 'get_image', 'date')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="70"')

    get_image.short_description = 'Picture'


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('instrument_category', 'status')
    readonly_fields = ['date']
    actions = [make_published, make_draft]
    list_display = ('name', 'status', 'get_image', 'date')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="70"')

    get_image.short_description = 'Picture'


@admin.register(BannerItems)
class BanneritemAdmin(admin.ModelAdmin):
    search_fields = ['Image_name']
    list_filter = ('status',)
    readonly_fields = ['date']
    actions = [make_published, make_draft]
    list_display = ('Image_name', 'status', 'get_image', 'date')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="70"')

    get_image.short_description = 'Picture'


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    actions = [make_published, make_draft]
    list_display = ('name', 'status', 'get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="70"')

    get_image.short_description = 'Picture'


admin.site.site_title = 'Medical Instruments Admin'
admin.site.site_header = 'Medical Instruments Admin'

