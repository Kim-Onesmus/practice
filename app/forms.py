from django import forms
from .models import Locate

class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = Locate
        fields = ('destination',)