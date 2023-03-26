from django.contrib import admin
from .models import PicData, TempData


@admin.register(PicData)
class PicDataAdmin(admin.ModelAdmin):
    list_display = ['chunk_id', 'chip', 'is_full', 'is_ready']
    list_filter = ['chunk_id', 'chip', 'is_full', 'is_ready']
    search_fields = ['chunk_id', 'chip']


@admin.register(TempData)
class TempDataDataAdmin(admin.ModelAdmin):
    list_display = ['chunk_id', 'index']
    list_filter = ['chunk_id', 'index']
    search_fields = ['chunk_id']
