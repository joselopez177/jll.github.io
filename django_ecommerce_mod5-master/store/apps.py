from django.apps import AppConfig
from django.db.models import BigAutoField






class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Debe ser una cadena
    name = 'store'