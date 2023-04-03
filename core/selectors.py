from django.db.models import QuerySet
from .models import TempData, PicData


def get_pic_chunks(chunk_id: str) -> QuerySet[TempData]:
    data = TempData.objects.filter(chunk_id=chunk_id).order_by('index')
    return data


def retrieve_pic_object(chunk_id: str) -> PicData:
    data, _ = PicData.objects.get_or_create(chunk_id=chunk_id)
    return data
