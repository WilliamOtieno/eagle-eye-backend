import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import TempData, PicData


@method_decorator(csrf_exempt, name='dispatch')
class PicDataView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET method ok')

    def post(self, request, *args, **kwargs):
        d = self.request.body.decode('utf-8')
        data = json.loads(d)
        if data.get('id') is not None:
            temp = TempData.objects.create(
                chunk_id=data.get('id'),
                index=data.get('index'),
                payload=data
            )
            PicData.objects.get_or_create(chunk_id=temp.chunk_id, chip=temp.chip)
        else:
            print('Empty Data Received')
        return HttpResponse('ok')
