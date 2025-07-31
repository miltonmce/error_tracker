import traceback
from django.http import JsonResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from .models import ErrorLog
import logging

logger = logging.getLogger(__name__)

class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Ignorar excepciones específicas que no queremos registrar
        if isinstance(exception, PermissionDenied):
            return None
        
        # Obtener el traceback completo
        tb = traceback.format_exc()
        
        # Determinar el código de estado (si es una excepción HTTP)
        status_code = 500
        if hasattr(exception, 'status_code'):
            status_code = exception.status_code
        
        # Guardar en la base de datos
        ErrorLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            path=request.path,
            method=request.method,
            error_message=str(exception),
            traceback=tb,
            status_code=status_code,  # Nuevo campo que añadimos
        )
        
        # Registrar el error
        logger.error(
            f"Error en la vista: {request.path}\n"
            f"Usuario: {request.user if hasattr(request, 'user') else 'Anónimo'}\n"
            f"Método: {request.method}\n"
            f"Código de estado: {status_code}\n"
            f"Excepción: {str(exception)}\n"
            f"Traceback:\n{tb}"
        )
        
        # Si quieres devolver una respuesta personalizada en DEBUG
        if settings.DEBUG:
            return JsonResponse({
                'error': str(exception),
                'status_code': status_code,
                'traceback': tb.split('\n'),
            }, status=status_code)
        
        return None  # Django manejará la excepción normalmente