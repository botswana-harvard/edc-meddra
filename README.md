# edc-meddra
Integrate EDC with MedDRA API, to connect to the dictionary. Performs search and get detail on reported search terms.
This module implements `django-autocomplete-light` module for lookup widget, autocompletion and rendering results to the user on the django admin during search.
Further details on the module can be found here: https://django-autocomplete-light.readthedocs.io/en/master/install.html

# Installation
`Install django-autocomplete-light`
    pip install django-autocomplete-light
`Install latest meddra module`
    pip install git+https://github.com/botswana-harvard/edc-meddra.git@develop#egg=edc_meddra

# Configuration
Add `dal`, `dal_select2` and `edc_meddra.apps.AppConfig` to INSTALLED_APPS and medDRA client configurations in your Django project settings.

    `settings.py`

        ....	
        APP_NAME = 'your_app_name'

        INSTALLED_APPS = (
          ...
          'dal',
          'dal_select2',
          'django.contrib.admin',
          ...
          'edc_odk.apps.AppConfig',
        )

        ODK_CONFIGURATION = {
              'OPTIONS': {
                    'read_default_file': '/etc/your_app_name/meddra.conf',
              },
        }

Run migrations and apply them:
