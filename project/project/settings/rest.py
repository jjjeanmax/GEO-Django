REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework_gis.schema.GeoFeatureAutoSchema',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.BaseFilterBackend',)
}