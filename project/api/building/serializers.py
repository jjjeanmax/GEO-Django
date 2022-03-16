from rest_framework_gis import serializers

from building.models import Building


class BuildingSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ('id', 'address')
        geo_field = 'geom'
        model = Building
