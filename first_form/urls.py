from django.urls import path

from first_form.views import index

app_name = "firstform"

urlpatterns = [path('', index, name='index'), ]
