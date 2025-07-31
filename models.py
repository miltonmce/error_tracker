# error_tracker/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class ErrorLog(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    error_message = models.TextField()
    traceback = models.TextField()
    status_code = models.PositiveIntegerField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolved_by = models.ForeignKey(
        User, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='resolved_errors'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Error en {self.path} ({self.created_at})"

    def mark_as_resolved(self, user):
        self.resolved = True
        self.resolved_at = timezone.now()
        self.resolved_by = user
        self.save()

    class Meta:
        verbose_name = "Error Log"
        verbose_name_plural = "Error Logs"
        ordering = ['-created_at']