from django.urls import path
from . import views


urlpatterns = [
    path('', views.PicDataView.as_view()),
]
