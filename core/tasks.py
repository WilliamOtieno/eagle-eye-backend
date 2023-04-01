from celery import shared_task

from .models import PicData
from .services import generate_image_from_chunks


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 5})
def process_payload():
    data_ = PicData.objects.filter(is_processed=False, is_full=True, is_ready=True)
    for data in data_:
        generate_image_from_chunks(chunk_id=data.chunk_id)
