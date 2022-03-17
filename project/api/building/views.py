from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_gis.filters import DistanceToPointFilter

from building.models import Building
from rest_framework.decorators import action

from .filter import AreaFilter
from .serializers import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    """
    -создавать, изменять, удалять и получать записи таблицы building

    -BuildingSerializer: валидатор, проверяющий геометрию объекта на валидность при добавлении
        или изменении записи

    -DistanceToPointFilter :позволяющий отфильтровывать возвращаемые геометрические
      объекты в зависимости от их расстояния от заданной точки
        :param : dist и point
    """

    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    distance_filter_field = 'geom'
    filter_backends = (DistanceToPointFilter,)

    # Второй вариант
    @action(detail=False, methods=['get'])
    def filter_by_area(self, request):
        try:
            aire = round(float(request.GET['area']), 8)
            qs_are = Building.qs.air()
            queryset = Building.objects.get(pk=qs_are[aire])
            serialize = BuildingSerializer(queryset)
            return Response(status=status.HTTP_200_OK, data=serialize.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"Message": 'area Parameter is missing or Not Found Objects !'})


class AreaGetBuildingViewSet(viewsets.ModelViewSet):
    """
    -AreaFilter :фильтр, позволяющий отфильтровывать возвращаемые геометрические
   объекты в зависимости от их площади.

        :param: значение минимальной и (или) максимальной площади полигона
   в квадратных метрах (8-digit -> округление)
    """

    filter_backends = (AreaFilter,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    bbox_filter_include_overlapping = True  # Optional
