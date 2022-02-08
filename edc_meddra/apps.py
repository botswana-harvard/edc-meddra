from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_meddra'
    verbose_name = 'Edc Meddra'
    version = None
