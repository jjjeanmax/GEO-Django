import json
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured


#################################
# Конфигурационный файл
#################################

secrets_path = os.path.join(Path(__file__).resolve().parent, 'configs.json')
with open(secrets_path) as f:
    secrets_data = json.loads(f.read())


def get_secret(setting, section=None, secrets=None):
    if secrets is None:
        secrets = secrets_data

    try:
        if section:
            return secrets[section][setting]
        return secrets[setting]
    except KeyError:
        key = setting if not section else '%s["%s"]' % (section, setting)
        error_message = 'Secrets: {} key not found in configs.json.'.format(key)
        raise ImproperlyConfigured(error_message)
