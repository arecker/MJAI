from django.contrib import admin
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_thumb', 'filename', 'gallery']


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    """Delete associated file when image is deleted"""
    instance.file.delete(False)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        ImageInline,
    ]


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)