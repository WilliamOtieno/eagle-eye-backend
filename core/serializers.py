from rest_framework.serializers import ModelSerializer
from .models import PicData


class PicDataSerializer(ModelSerializer):

    class Meta:
        model = PicData
        exclude = ['vision']
