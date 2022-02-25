from dal import autocomplete
from django import forms


class MedDRAFormMixin(forms.ModelForm):

    search_code = forms.CharField(
        label='Search MedDRA dictionary',
        widget=autocomplete.ListSelect2(url='edc_meddra:ae-term-autocomplete'),
        required=False)
