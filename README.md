
---

# Django Error Tracker

**A robust error tracking and management system for Django applications**

This Django application provides comprehensive error tracking capabilities through middleware that automatically captures, logs, and manages exceptions occurring in your Django project.

## Key Features

- **Automatic Error Capture**: Middleware that intercepts and records all unhandled exceptions
- **Detailed Error Logging**: Stores complete error details including:
  - Traceback information
  - Request metadata (path, method, user)
  - Timestamps
  - Status codes
- **Admin Integration**: Full-featured Django admin interface for error management
- **Error Resolution Workflow**: Mark errors as resolved/unresolved with tracking
- **Search & Filtering**: Powerful tools to find and analyze errors
- **Debugging Support**: Enhanced JSON error responses in development mode

## Implementation Highlights

- **Middleware-based**: Lightweight, non-intrusive integration
- **Database Backed**: Uses Django models for error storage
- **Permission Controlled**: Secure access to error information
- **Production Ready**: Handles errors gracefully in production environments
- **Developer Friendly**: Detailed error information during development

## Ideal For

- Production Django applications needing error monitoring
- Development teams wanting better exception visibility
- Projects requiring historical error tracking
- Applications without external error tracking services

## Quick Start (Development Installation)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-error-tracker.git
   ```

2. Add to your Django project:
   ```python
   # settings.py
   INSTALLED_APPS = [
       ...
       'error_tracker',
   ]

   MIDDLEWARE = [
       ...
       'error_tracker.middleware.ErrorLoggingMiddleware',
   ]
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Access errors via:
   - Custom dashboard: `/error-tracker/`

---
