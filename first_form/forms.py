from django import forms
from first_form.models import Person


class TriangleForm(forms.Form):

    leg_a = forms.IntegerField(label="leg_a", min_value=0, required=True)
    leg_b = forms.IntegerField(label="leg_b", min_value=0, required=True)


class PersonModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
