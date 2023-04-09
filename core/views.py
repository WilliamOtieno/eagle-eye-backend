import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import TempData, PicData
from .tasks import process_payload


@method_decorator(csrf_exempt, name='dispatch')
class PicDataView(View):

    def get(self, request, *args, **kwargs):
        pics = PicData.objects.filter(is_processed=True)
        context = {'pics': pics}
        return render(self.request, 'core/index.html', context)

    def post(self, request, *args, **kwargs):
        d = self.request.body.decode('utf-8')
        data = json.loads(d)
        chunk_str = data.get('id')
        if chunk_str is not None:
            chunk_id = chunk_str.split('-')[-1]
            pic_id = f"{chunk_str.split('-')[0]}-{chunk_str.split('-')[1]}"
            temp = TempData.objects.create(
                chunk_id=chunk_id,
                pic_id=pic_id,
                index=data.get('index'),
                payload=data
            )
            p, _ = PicData.objects.get_or_create(pic_id=pic_id)
            if temp.is_last_chunk:
                p.is_full = True
                p.is_ready = True
                p.save()
        else:
            print('Empty Data Received')
        return HttpResponse('ok')
