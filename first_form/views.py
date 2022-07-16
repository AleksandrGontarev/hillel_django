from django.shortcuts import get_object_or_404, redirect, render

from first_form.models import Person

from .forms import PersonModelForm, TriangleForm


def index(request):

    hypotenuse = None
    if "submit" in request.GET:
        triangle_form = TriangleForm(request.GET)
        if triangle_form.is_valid():
            leg_a = triangle_form.cleaned_data["leg_a"]
            leg_b = triangle_form.cleaned_data["leg_b"]
            hypotenuse = (leg_a**2 + leg_b**2)**1/2
    else:
        triangle_form = TriangleForm()
    return render(
        request,
        "first_form/form.html",
        {"triangle_form": triangle_form,
         "hypotenuse": hypotenuse},
    )


def model_form(request):
    if request.method == 'POST':
        person_form = PersonModelForm(data=request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('firstform:person-form')
    else:
        person_form = PersonModelForm()
    return render(request,
                  "first_form/person_model_from.html",
                  {
                      'person_form': person_form,
                  }
                  )


def model_update_form(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person_form = PersonModelForm(data=request.POST, instance=obj)
        if person_form.is_valid():
            person_form.save()
            return redirect('firstform:person-update-form')
    else:
        person_form = PersonModelForm(instance=obj)
    return render(request,
                  "first_form/update_model_form.html",
                  {
                      'person_form': person_form,
                      'obj': obj,
                  }
                  )
