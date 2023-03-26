from django.db import models


class TimestampedModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PicData(TimestampedModel):
    chunk_id = models.CharField(max_length=256)
    chip = models.CharField(max_length=256)
    vision = models.TextField()
    length = models.BigIntegerField(default=0)
    batt = models.IntegerField(default=0)
    is_full = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)


class TempData(TimestampedModel):
    chunk_id = models.CharField(max_length=256)
    index = models.IntegerField(default=0)
    payload = models.JSONField(null=True, blank=True)

    @property
    def is_last_chunk(self) -> bool:
        return self.payload.get('length') is not None
