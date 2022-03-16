from .secret import get_secret


#################################
# База данных
#################################

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': get_secret(section='DATABASE', setting='HOST'),
        'PORT': get_secret(section='DATABASE', setting='PORT'),
        'NAME': get_secret(section='DATABASE', setting='NAME'),
        'USER': get_secret(section='DATABASE', setting='USER'),
        'PASSWORD': get_secret(section='DATABASE', setting='PASSWORD'),
    }
}
