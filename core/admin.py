from django.contrib import admin
from .models import PicData, TempData


@admin.register(PicData)
class PicDataAdmin(admin.ModelAdmin):
    list_display = ['pic_id', 'chip', 'is_full', 'is_ready', 'is_processed', 'created', 'updated']
    list_filter = ['pic_id', 'chip', 'is_full', 'is_ready', 'is_processed', 'created', 'updated']
    search_fields = ['pic_id', 'chip']


@admin.register(TempData)
class TempDataDataAdmin(admin.ModelAdmin):
    list_display = ['pic_id', 'chunk_id', 'index']
    list_filter = ['pic_id', 'index']
    search_fields = ['pic_id', 'chunk_id']
