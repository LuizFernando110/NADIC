from functools import wraps
from django.http import HttpResponseForbidden

def patrao_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.patrao:
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view