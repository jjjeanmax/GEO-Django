# GEO-Django
Working with spatial data, coordinate systems, spatial database queries, calculating distances and areas on an ellipsoid


# Requirement:

- Database: PostgreSQL 10.0 or higher with PostGIS 3.0 extension or higher.
- Programming language: Python 3.8 or higher.
- Python libraries: Django 3.2 or higher, Django REST Framework 3.12 or higher,
  psycopg2 2.8 or higher.
- Additional system libraries required to work with spatial
  Data: GDAL 3.0 or higher, PROJ 6.0 or higher, GEOS 3.6 or higher.
- Desktop applications for preparing and viewing spatial data
  (optional, may be useful for testing): QGIS 3.x.

Job content
------------------

Django + Django REST Framework.

1. Add an application to the project with a Building model that describes a geographic
   the location and address of the building. The following fields are required:
   - id - integer primary key with auto increment;
   - geom - polygonal geometry in WGS84 coordinate system (EPSG:4326);
   - address - text string to store the postal address of the building.

2. Implement a REST API for CRUD based on ModelViewSet that allows you to create,
   modify, delete, and retrieve records in the building table. Must be supported
   GeoJSON spatial data format (RFC 7946). When accessing elements
   collections by id (methods GET, POST, UPDATE) must be passed or returned
   an object of type Feature, when accessing the collection as a whole (GET method) - an object
   FeatureCollection from the GeoJSON specification. Pagination of results is not required.

3. Add a validator that checks the geometry of the object for validity when added
   or change the entry.

4. Add a filter that allows you to filter the returned geometric
   objects according to their area. The filter must accept in parameters
   GET request value of the minimum and (or) maximum area of ​​the polygon
   in square meters.

5. Add a filter that allows you to filter the returned geometric
   objects based on their distance from a given point. The filter must accept point coordinates (longitude and latitude) as parameters of the GET request.
   in the WGS84 coordinate system) and the maximum distance in meters.
   Objects that fall completely within the given radius should be returned.
   or partially.

6. Add tests to the project that check the correct operation of the filters.


## Configuration file
When deploying, copy the `configs.json.example` file to the `configs.json` file in the directory
`project/project/settings/`.

Example `configs.json` file `project/project/settings/configs.json.example`.

## Start

1. Create and activate virtual environment:

    `python -m venv venv`

2. Install packages:

    `pip install -r requirements.txt`

3. Run migrations:

    `python manage.py migrate`

4. Create superuser:

    `python manage.py createsuperuser`

4. Create config file:

    `configs.json`

6. Start django server:
    
    `$ python manage.py runserver`

7. Start telegram server from BOT repository:
    
    `$ python main.py`

### Documentation is available in docs:
>  http://127.0.0.1:8000/api/redoc/
