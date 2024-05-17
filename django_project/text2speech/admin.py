from django.contrib import admin
from .models import MP3File

# Register your models here.
class MP3FileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'text',
        'file_location',
        'owner',
        'created_at',
    ]

admin.site.register(MP3File, MP3FileAdmin)