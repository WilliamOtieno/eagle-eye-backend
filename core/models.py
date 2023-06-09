from django.db import models


class TimestampedModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PicData(TimestampedModel):
    pic_id = models.CharField(max_length=256, null=True, blank=True)
    chip = models.CharField(max_length=256, null=True, blank=True)
    vision = models.TextField(default='')
    length = models.BigIntegerField(default=0)
    batt = models.IntegerField(default=0)
    is_full = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)


class TempData(TimestampedModel):
    chunk_id = models.CharField(max_length=256, null=True, blank=True)
    pic_id = models.CharField(max_length=256, null=True, blank=True)
    index = models.IntegerField(default=0)
    payload = models.JSONField(null=True, blank=True)

    @property
    def is_last_chunk(self) -> bool:
        return self.payload.get('length') is not None

    @property
    def chip(self):
        return self.payload.get('chip')
