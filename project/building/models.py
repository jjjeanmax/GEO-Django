from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db import models


class BuildingQuerySet(models.QuerySet):
    def area(self):
        all_airea = {}
        _all = list(super().values('geom', 'id'))
        for a in _all:
            # тут выбираю 8 знаков после запятой
            all_airea[(round(GEOSGeometry(a['geom']).area, 8))] = a['id']
        return all_airea


class BuildingManager(models.Manager):
    def get_queryset(self):
        return BuildingQuerySet(self.model, using=self._db)

    def air(self):
        return self.get_queryset().area()


class Building(models.Model):
    geom = models.PolygonField(srid=4326, geography=True, verbose_name="полигональная геометрия")
    address = models.CharField(max_length=255, verbose_name="почтовый адреса строения")
    objects = models.Manager()
    qs = BuildingManager()

    class Meta:
        verbose_name = 'Строение'
        verbose_name_plural = 'Строения'

    def __str__(self):
        return str(self.address)
