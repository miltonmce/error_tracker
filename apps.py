from django.apps import AppConfig


class ErrorTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.error_tracker'

    def ready(self):
        # Importa las señales si las añades después
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from .models import ErrorLog
        
        # Crea permisos personalizados si es necesario
        content_type = ContentType.objects.get_for_model(ErrorLog)