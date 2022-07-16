from django.utils.deprecation import MiddlewareMixin

from first_form.models import Log


class LogMiddleware(MiddlewareMixin):

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.path.startswith('/admin'):
            path = request.path
            method = request.method
            Log.objects.create(path=path, method=method)
