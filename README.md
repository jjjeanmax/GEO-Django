# GEO-Django
Работа с пространственными данными, системы координат,  пространственные запросы к БД, вычисления расстояний и площадей на эллипсоиде


# Требование:

- База данных: PostgreSQL 10.0 или выше с расширением PostGIS 3.0 или выше.
- Язык программирования: Python 3.8 или выше.
- Библиотеки Python: Django 3.2 или выше, Django REST Framework 3.12 или выше,
  psycopg2 2.8 или выше.
- Дополнительные системные библиотеки, необходимые для работы с пространственными
  данными: GDAL 3.0 или выше, PROJ 6.0 или выше, GEOS 3.6 или выше.
- Десктопные приложения для подготовки и просмотра пространственных данных
  (опционально, может быть полезным при тестировании): QGIS 3.x.

Содержание задания
------------------

Django + Django REST Framework.

1. Добавить в проект приложение с моделью Building, описывающую географическое
   положение и адрес строения. Требуются следующие поля:
   - id  - целочисленный первичный ключ с автоинкрементом;
   - geom - полигональная геометрия в системе координат WGS84 (EPSG:4326);
   - address - текстовая строка для хранения почтового адреса строения.

2. Реализовать REST API для CRUD на базе ModelViewSet, позволяющий создавать,
   изменять, удалять и получать записи таблицы building. Должен поддерживаться
   формат пространственных данных GeoJSON (RFC 7946). При обращении к элементам
   коллекции по id (методы GET, POST, UPDATE) должен передаваться или возвращаться
   объект типа Feature, при обращении к коллекции в целом (метод GET) - объект
   FeatureCollection из спецификации GeoJSON. Пагинация результатов не требуется.

3. Добавить валидатор, проверяющий геометрию объекта на валидность при добавлении
   или изменении записи.

4. Добавить фильтр, позволяющий отфильтровывать возвращаемые геометрические
   объекты в зависимости от их площади. Фильтр должен принимать в параметрах
   GET-запроса значение минимальной и (или) максимальной площади полигона
   в квадратных метрах.

5. Добавить фильтр, позволяющий отфильтровывать возвращаемые геометрические
   объекты в зависимости от их расстояния от заданной точки. Фильтр должен принимать в параметрах GET-запроса координаты точки (долготу и широту
   в системе координат WGS84) и максимальное расстояние в метрах.
   Должны возвращаться объекты, попадающие в заданный радиус полностью
   или частично.

6. Добавить в проект тесты, проверяющие правильность работы фильтров.


## Конфигурационный файл
При развертывание скопировать файл `configs.json.example` в файл `configs.json` в директории 
`project/project/settings/`.

Пример `configs.json` файла `project/project/settings/configs.json.example`.

## Старт

1. Создать и активировать виртуальное окружение:

    `python -m venv venv`


2. Установить пакеты:

    `pip install -r requirements.txt`


3. Выполнить команду для выполнения миграций :

    `python manage.py migrate`


4. Создать статичные файлы: 

    `python manage.py collectstatic`


5. Создать суперпользователя:

    `python manage.py createsuperuser`


6. Запустить сервер:

    `$ python manage.py runserver`

7. Документация:

   http://127.0.0.1:8000/api/redoc/
