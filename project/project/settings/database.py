from .secret import get_secret, get_secrets

#################################
# База данных
#################################

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': get_secret(section='DATABASE', setting='default')['HOST'],
        'PORT': get_secret(section='DATABASE', setting='default')['PORT'],
        'NAME': get_secret(section='DATABASE', setting='default')['NAME'],
        'USER': get_secret(section='DATABASE', setting='default')['USER'],
        'PASSWORD': get_secret(section='DATABASE', setting='default')['PASSWORD'],

        'TEST': {'NAME': get_secret(section='DATABASE', setting='default')['TEST']['NAME'],
                 }
    }
}
