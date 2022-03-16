import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_gis.filters import DistanceToPointFilter

from building.models import Building
from rest_framework.decorators import action

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

    distance_filter_field = 'geom'
    distance_filter_convert_meters = True
    filter_backends = (DistanceToPointFilter,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    bbox_filter_include_overlapping = True  # Optional

    @action(detail=False, methods=['get'])
    def filter_by_aera(self, request):
        try:
            aire = request.GET['area']
            qs_are = Building.qs.air()

            for v, k in qs_are.items():
                if float(v) != float(aire):
                    return Response(status=status.HTTP_404_NOT_FOUND)
                qs = Building.objects.all().get(pk=k)

                serialize = BuildingSerializer(qs)
                return Response(status=status.HTTP_200_OK, data=serialize.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"Message": 'No Matched !'})


class AreaGetBuildingViewSet(viewsets.ModelViewSet):
    # Тоже Работает
    """
        :AreaFilter :фильтр, позволяющий отфильтровывать возвращаемые геометрические
   объекты в зависимости от их площади.

        :param: значение минимальной и (или) максимальной площади полигона
   в квадратных метрах (8-digit -> округление)
    """

    filter_backends = (AreaFilter,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    bbox_filter_include_overlapping = True  # Optional
