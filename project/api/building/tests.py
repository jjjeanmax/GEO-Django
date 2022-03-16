import json
import urllib
from unittest import skipIf

from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry
from django.test import TestCase, AsyncRequestFactory
from django.urls import reverse

from building.models import Building
from .views import (
    BuildingViewSet,
)

has_spatialite = (
        settings.DATABASES['default']['ENGINE']
        == 'django.contrib.gis.db.backends.spatialite'
)

try:
    from django.contrib.gis.db.models.functions import GeometryDistance

    has_geometry_distance = GeometryDistance and True
except ImportError:
    has_geometry_distance = False


class TestRestFrameworkGisFilters(TestCase):

    client = AsyncRequestFactory()
    view = BuildingViewSet.as_view({'get': 'filter_by_aera'})
    """
    unit tests for filters 
    """

    def setUp(self):
        self.location_within_distance_of_point_list_url = reverse(
            'api_building_within_distance_of_point_list_url'
        )

        self.building_within_area_url = reverse('api_building_within_area_url')

        corberon_geojson = """{
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -122.44640350341795,
                        37.86103094116189
                    ],
                    [
                        -122.44262695312501,
                        37.85506751416839
                    ],
                    [
                        -122.43481636047363,
                        37.853305500228025
                    ],
                    [
                        -122.42975234985352,
                        37.854660899304704
                    ],
                    [
                        -122.41953849792479,
                        37.852627791344894
                    ],
                    [
                        -122.41807937622069,
                        37.853305500228025
                    ],
                    [
                        -122.41868019104004,
                        37.86211514878027
                    ],
                    [
                        -122.42391586303711,
                        37.870584971740065
                    ],
                    [
                        -122.43035316467285,
                        37.8723465726078
                    ],
                    [
                        -122.43515968322752,
                        37.86963639998042
                    ],
                    [
                        -122.43953704833984,
                        37.86882332875222
                    ],
                    [
                        -122.44640350341795,
                        37.86103094116189
                    ]
                ]
            ],
            "properties": {
                "address": "corberon"
            }
        }"""
        self.corberon_geom = GEOSGeometry(corberon_geojson)

        corgegoux2_geojson = """{
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -122.5111198425293,
                        37.77125750792944
                    ],
                    [
                        -122.51026153564452,
                        37.76447260365713
                    ],
                    [
                        -122.45309829711913,
                        37.76677954095475
                    ],
                    [
                        -122.45481491088867,
                        37.77424266859531
                    ],
                    [
                        -122.5111198425293,
                        37.77125750792944
                    ]
                ]
            ],
             "properties": {
                "address": "corgegoux2"
            }
        }"""
        self.corgegoux2_geom = GEOSGeometry(corgegoux2_geojson)

    @skipIf(
        has_spatialite, 'Skipped test for spatialite backend: missing feature "dwithin"'
    )
    def test_DistanceToPointFilter_filtering(self):
        """
        Checks that the DistanceFilter returns only objects within the given distance of the
        given geometry defined by the URL parameters
        """
        self.assertEqual(Building.objects.count(), 0)

        # Filter parameters
        distance = 5000  # meters
        point_on_alcatraz = [-122.4222, 37.82667]

        url_params = '?dist=%0.4f&point=hello&format=json' % (distance,)
        response = self.client.get(
            '%s%s' % (self.location_within_distance_of_point_list_url, url_params)
        )
        self.assertEqual(response.status_code, 400)

        url_params = '?dist=%0.4f&point=%0.4f,%0.4f&format=json' % (
            distance,
            point_on_alcatraz[0],
            point_on_alcatraz[1],
        )

        corberon = Building()
        corberon.address = "corberon"
        corberon.geom = self.corberon_geom
        corberon.full_clean()
        corberon.save()

        corgegoux2 = Building()
        corgegoux2.address = "corgegoux2"
        corgegoux2.geom = self.corgegoux2_geom
        corgegoux2.save()

        # Get back the ones within the distance
        response = self.client.get(
            '%s%s' % (self.location_within_distance_of_point_list_url, url_params)
        )
        self.assertEqual(len(response.data['features']), 1)
        for result in response.data['features']:
            self.assertEqual(result['properties']['address'], corberon.address)

        # Get back all the ones within the distance
        distance = 7000
        url_params = '?dist=%0.4f&point=%0.4f,%0.4f&format=json' % (
            distance,
            point_on_alcatraz[0],
            point_on_alcatraz[1],
        )
        response = self.client.get(
            '%s%s' % (self.location_within_distance_of_point_list_url, url_params)
        )
        self.assertEqual(len(response.data['features']), 2)
        for result in response.data['features']:
            self.assertIn(
                result['properties']['address'], (corgegoux2.address, corberon.address)
            )

    @skipIf(
        has_spatialite, 'Skipped test for spatialite backend: missing feature "dwithin"'
    )
    def test_AreaFilter(self):
        """
        Checks that the DistanceFilter returns only objects within the given distance of the
        given geometry defined by the URL parameters
        """
        self.assertEqual(Building.objects.count(), 0)

        # Filter parameters
        area = 0.00039117  # meters^2

        url_params = '?area=%f&format=json' % (area,)
        response = self.client.get(
            '%s%s' % (self.location_within_distance_of_point_list_url, url_params)
        )
        self.assertEqual(response.status_code, 200)

        url_params = '?area=%f&format=json' % (area,)
        corberon = Building()
        corberon.id = 3
        corberon.address = "corberon"
        corberon.geom = self.corberon_geom
        corberon.full_clean()
        corberon.save()

        corgegoux2 = Building()
        corgegoux2.id = 4
        corgegoux2.address = "corgegoux2"
        corgegoux2.geom = self.corgegoux2_geom
        corgegoux2.save()

        corberon_area = round(GEOSGeometry(self.corberon_geom).area, 8)
        corgegoux2_area = round(GEOSGeometry(self.corgegoux2_geom).area, 8)
        qs_all = Building.qs.air()

        self.assertEqual(tuple((qs_all.keys())), (corberon_area, corgegoux2_area))

        response = self.client.get(
            '%s%s' % (self.location_within_distance_of_point_list_url, url_params)
        )

        for result in response.data['features']:
            self.assertNotEqual(result['id'], (corberon.id,))

        area = 0.00040758  # meters^2
        url_params = '?area=%f&format=json' % (area,)

        response = self.client.get(
            '%s%s' % (self.location_within_distance_of_point_list_url, url_params)
        )

        for result in response.data['features']:
            self.assertNotEqual(result['id'], (corgegoux2.id,))
