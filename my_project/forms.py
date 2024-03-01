from urllib import request

from django import forms
from my_project.models import *
from django.core.exceptions import ValidationError

class CharForm(forms.Form):
    model = forms.CharField(help_text="Введите модель")
    price = forms.IntegerField(help_text="Введите цену", min_value=1)

    transmission = forms.ModelChoiceField(
        queryset=Transmission.objects.filter(), help_text="Выберите коробку передач")

    bodywork = forms.ModelChoiceField(
        queryset=Bodywork.objects.filter(), help_text="Выберите кузов")

    class Meta:
        model = Transmission
        fields = ['type_of_transmission']



    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise ValidationError("Стоимость не может быть отрицательной!")
        return price
