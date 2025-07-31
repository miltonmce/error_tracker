from django.urls import path
from . import views

app_name = 'error_tracker'

# error_tracker/urls.py
from django.urls import path
from . import views

app_name = 'error_tracker'

urlpatterns = [
    path('trigger-error/', views.trigger_error, name='trigger-error'),
    path('', views.error_list, name='error_list'),
    path('errors/<int:error_id>/', views.error_detail, name='error_detail'),
    path('errors/<int:error_id>/resolve/', views.mark_error_resolved, name='mark_resolved'),
    path('errors/<int:error_id>/unresolve/', views.mark_error_unresolved, name='mark_unresolved'),
]