from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter

from building.models import Building

from .filter import AreaFilter
from .serializers import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    """
    создавать, изменять, удалять и получать записи таблицы building

    :BuildingSerializer: валидатор, проверяющий геометрию объекта на валидность при добавлении
        или изменении записи

    :DistanceToPointFilter :позволяющий отфильтровывать возвращаемые геометрические
      объекты в зависимости от их расстояния от заданной точки
        :param : dist и point
    """

    bbox_filter_field = 'geom',
    filter_backends = (DistanceToPointFilter,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    bbox_filter_include_overlapping = True  # Optional


class AreaGetBuildingViewSet(viewsets.ModelViewSet):
    """
        :AreaFilter :фильтр, позволяющий отфильтровывать возвращаемые геометрические
   объекты в зависимости от их площади.

        :param: значение минимальной и (или) максимальной площади полигона
   в квадратных метрах (8-digit -> округление)
    """

    filter_backends = (AreaFilter, )
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    bbox_filter_include_overlapping = True  # Optional
