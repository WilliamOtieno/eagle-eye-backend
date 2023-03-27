import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import TempData


@method_decorator(csrf_exempt, name='dispatch')
class PicDataView(View):

    def get(self, request, *args, **kwargs):
        print('GET Request:......')
        print(self.request.GET)
        print('GET Request:......')
        return HttpResponse('GET method ok')

    def post(self, request, *args, **kwargs):
        d = self.request.body.decode('utf-8')
        data = json.loads(d)
        print(data)
        if data.get('id') is not None:
            TempData.objects.create(
                chunk_id=data.get('id'),
                index=data.get('index'),
                payload=data
            )
        else:
            print('Empty Data Received')
        return HttpResponse('ok')
