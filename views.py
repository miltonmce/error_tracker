# error_tracker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ErrorLog

@login_required
@permission_required('error_tracker.add_errorlog', raise_exception=True)
def trigger_error(request):
    # This view is just for testing purposes to trigger an error
    raise Exception("This is a test error for the error tracker.")

@login_required
@permission_required('error_tracker.view_errorlog', raise_exception=True)
def error_list(request):
    # Filtros
    query = request.GET.get('q', '')
    resolved_filter = request.GET.get('resolved', 'all')
    
    errors = ErrorLog.objects.all().order_by('-created_at')
    
    if query:
        errors = errors.filter(
            Q(path__icontains=query) |
            Q(error_message__icontains=query) |
            Q(method__icontains=query)
        )
    
    if resolved_filter == 'resolved':
        errors = errors.filter(resolved=True)
    elif resolved_filter == 'unresolved':
        errors = errors.filter(resolved=False)
    
    # Paginación
    paginator = Paginator(errors, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'resolved_filter': resolved_filter,
    }
    return render(request, 'error_tracker/error_list.html', context)

@login_required
@permission_required('error_tracker.view_errorlog', raise_exception=True)
def error_detail(request, error_id):
    error = ErrorLog.objects.get(id=error_id)
    traceback_lines = error.traceback.split('\n') if error.traceback else []
    
    context = {
        'error': error,
        'traceback_lines': traceback_lines,
    }
    return render(request, 'error_tracker/error_detail.html', context)

@login_required
@permission_required('error_tracker.change_errorlog', raise_exception=True)
def mark_error_resolved(request, error_id):
    error = ErrorLog.objects.get(id=error_id)
    error.mark_as_resolved(request.user)
    return redirect('error_tracker:error_detail', error_id=error.id)

@login_required
@permission_required('error_tracker.change_errorlog', raise_exception=True)
def mark_error_unresolved(request, error_id):
    error = ErrorLog.objects.get(id=error_id)
    error.resolved = False
    error.resolved_at = None
    error.resolved_by = None
    error.save()
    return redirect('error_tracker:error_detail', error_id=error.id)