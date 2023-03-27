from celery import shared_task

from .models import PicData
from .services import generate_image_from_chunks


@shared_task
def process_payload():
    data_ = PicData.objects.filter(is_full=True, is_ready=False)
    for data in data_:
        generate_image_from_chunks(chunk_id=data.chunk_id)
