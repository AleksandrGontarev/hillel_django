from django import forms


class TriangleForm(forms.Form):

    leg_a = forms.IntegerField(label="leg_a", min_value=0, required=True)
    leg_b = forms.IntegerField(label="leg_b", min_value=0, required=True)
