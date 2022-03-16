from django.contrib.gis import admin

from .models import Building


@admin.register(Building)
class BuildingAdmin(admin.GISModelAdmin):
    list_display = ("id", "address", "geom",)
