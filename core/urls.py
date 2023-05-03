from django.urls import path
from . import views


urlpatterns = [
    path('', views.PicDataView.as_view()),
    path('api/', views.PicDataListView.as_view()),
]
