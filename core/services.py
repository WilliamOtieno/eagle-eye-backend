import base64
from io import BytesIO

from PIL import Image
from .selectors import get_pic_chunks, retrieve_pic_object


def resolve_b64_chunks(chunk_id):
    pic_object = retrieve_pic_object(chunk_id=chunk_id)
    temps = get_pic_chunks(chunk_id)
    for data in temps:
        pic_object.vision += data.payload['vision']
        if data.is_last_chunk:
            pic_object.is_full = True
    pic_object.save()
    return pic_object


def generate_image_from_chunks(chunk_id):
    obj = resolve_b64_chunks(chunk_id)
    img = Image.open(BytesIO(base64.b64decode(obj.vision.encode())))
    obj.image = img
    obj.is_ready = True
    obj.save()
