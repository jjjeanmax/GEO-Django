from django.urls import path

from .views import *

urlpatterns = [
    path('get-all/', BuildingViewSet.as_view({'get': 'list'})),
    path('get-by-id/<int:pk>/', BuildingViewSet.as_view({'get': 'retrieve'})),
    path('create/', BuildingViewSet.as_view({'post': 'create'})),
    path('put/', BuildingViewSet.as_view({'put': 'update'})),
    path('delete/<int:pk>/', BuildingViewSet.as_view({'delete': 'destroy'})),
    path('rename/geom/<int:pk>/', BuildingViewSet.as_view({'post': 'partial_update'})),
    path('get/in_bbox/', BuildingViewSet.as_view({'get': 'list'})),
    path('get-by/area/', AreaGetBuildingViewSet.as_view({'get': 'list'})),
]
