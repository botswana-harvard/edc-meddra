from django.contrib import admin
from django.urls import path

from .lookups import AETermAutocomplete
from . import views

app_name = 'edc_meddra'

urlpatterns = [
    path('meddra/detail/<slug:term_code>/', views.meddra_details, name='meddra-detail'),
    path('ae-term-autocomplete/', AETermAutocomplete.as_view(), name='ae-term-autocomplete'),
    path('admin/', admin.site.urls),
]
