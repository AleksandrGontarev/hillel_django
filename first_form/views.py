from django.shortcuts import render

from .forms import TriangleForm


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
