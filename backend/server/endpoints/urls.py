from django.urls import path, include
from .views import BaseRowsView, SingleRowView, ManyRowsView

urlpatterns = [
    path('get-data/', BaseRowsView.as_view(), name='base'),
    path('get-data/<id>', SingleRowView.as_view(), name='single'),
    path('get-data/<id_min>/<id_max>', ManyRowsView.as_view(), name='many'),
]