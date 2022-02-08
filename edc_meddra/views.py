from django.apps import apps as django_apps
from django.http.response import JsonResponse

from .classes import DetailsMedDRADict


def meddra_details(request, term_code):
    """ Endpoint to call detail function, and provide access.
    """
    version = django_apps.get_app_config('edc_meddra').version
    _meddra_details = DetailsMedDRADict(version=version)
    response = _meddra_details.details(code=term_code)
    return JsonResponse(response)
