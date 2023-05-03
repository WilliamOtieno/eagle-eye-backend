from rest_framework.serializers import ModelSerializer
from .models import PicData


class PicDataSerializer(ModelSerializer):

    class Meta:
        model = PicData
        fields = '__all__'
        exclude = ['vision']
