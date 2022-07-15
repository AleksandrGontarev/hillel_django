from django.urls import path

from first_form.views import index, model_form, model_update_form

app_name = "firstform"

urlpatterns = [
    path('triangle/', index, name='index'),
    path('person/', model_form, name='person-form'),
    path('person/<int:pk>/', model_update_form, name='person-update-form'),
]
