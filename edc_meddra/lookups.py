from dal import autocomplete
from django.apps import apps as django_apps
from django.contrib.auth.mixins import LoginRequiredMixin

from .classes import SearchMedDRADict


search_tuple = list()


class AETermAutocomplete(LoginRequiredMixin, autocomplete.Select2ListView):

    version = django_apps.get_app_config('edc_meddra').version

    @property
    def search_api(self):
        search_api = SearchMedDRADict
        return search_api(version=self.version)

    def get_list(self):
        global search_tuple
        qs = self.search_api.search(self.q)
        list_ = list()
        for dict_obj in qs:
            name = dict_obj.get('name', None)
            code = dict_obj.get('code', 0)
            search_tuple.append((code, name))
            list_.append((code, name, ))

        if self.q and self.q not in list_:
            # This allows new values to be created as the first option
            list_ = [(None, self.q, )] + list_
        return list_
