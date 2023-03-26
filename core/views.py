from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import TempData


@method_decorator(csrf_exempt, name='dispatch')
class PicDataView(View):
    def post(self, request, *args, **kwargs):
        TempData.objects.create(
            chunk_id=self.request.POST.get('id'),
            index=self.request.POST.get('index'),
            payload=self.request.POST
        )
        return HttpResponse('ok')
