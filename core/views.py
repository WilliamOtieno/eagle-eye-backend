from django.http import HttpResponse
from django.views import View

from .models import TempData


class PicDataView(View):
    def post(self, **kwargs):
        TempData.objects.create(payload=self.request.POST)
        return HttpResponse('ok')
