from django.conf.urls import url, include
from .views import ProductoList, ProductoCreate, ProductoDelete, ProductoUpdate, ProductoDetail

urlpatterns = [
    url(r'^$', ProductoList.as_view(), name = 'list'),
    url(r'^(?P<pk>\d+)$', ProductoDetail.as_view(), name = 'detail'),
    url(r'^nuevo$', ProductoCreate.as_view(), name = 'new'),
    url(r'^editar/(?P<pk>\d+)$', ProductoUpdate.as_view(), name = 'update'),
    url(r'^borrar/(?P<pk>\d+)$', ProductoDelete.as_view(), name = 'delete'),

    
]
