from django.db.models import QuerySet
from .models import TempData, PicData


def get_pic_chunks(pic_id: str) -> QuerySet[TempData]:
    data = TempData.objects.filter(pic_id=pic_id).order_by('index')
    return data


def retrieve_pic_object(pic_id: str) -> PicData:
    data, _ = PicData.objects.get_or_create(pic_id=pic_id)
    return data


def get_correct_pics():
    pics = PicData.objects.filter(
        is_processed=True
    ).order_by('-created')
    return pics
