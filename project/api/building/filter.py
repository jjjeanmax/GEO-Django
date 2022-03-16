from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import ParseError

from building.models import Building


class AreaFilter(BaseFilterBackend):
    area_param = 'area'  # The URL query parameter which contains the

    def get_filter_area(self, request, **kwargs):
        area = request.query_params.get(self.area_param, None)
        if not area:
            return None

        try:
            area_round = (round(float(area), 8))
        except ValueError:
            raise ParseError(
                'Invalid geometry string supplied for parameter {0}'.format(
                    self.area_param
                )
            )
        if area_round not in Building.qs.air().keys():
            return None

        return Building.qs.air()[area_round]

    def filter_queryset(self, request, queryset, view):
        try:
            _keys = self.get_filter_area(request)
            qs = Building.objects.filter(pk=_keys)
            return qs
        except TypeError as e:
            print(e)
