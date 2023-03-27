from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import TempData


@method_decorator(csrf_exempt, name='dispatch')
class PicDataView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET method ok')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.POST.keys())
        print(request.POST.values())
        if request.POST.get('id') is not None:
            TempData.objects.create(
                chunk_id=self.request.POST.get('id'),
                index=self.request.POST.get('index'),
                payload=self.request.POST
            )
        else:
            print('Empty Data Received')
        return HttpResponse('ok')
