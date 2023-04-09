import base64
import requests
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from .selectors import get_pic_chunks, retrieve_pic_object


def resolve_b64_chunks(pic_id: str):
    pic_object = retrieve_pic_object(pic_id=pic_id)
    temps = get_pic_chunks(pic_id)
    for data in temps:
        pic_object.vision += data.payload['vision']
    pic_object.save()
    return pic_object


def generate_image_from_chunks(pic_id):
    obj = resolve_b64_chunks(pic_id)
    parsed_string = requests.utils.unquote(obj.vision)
    img = ContentFile(base64.b64decode(parsed_string), name=f'{get_random_string(16)}.jpg')
    obj.image = img
    obj.is_processed = True
    obj.save()
