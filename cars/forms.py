"""
cars/forms.py
"""

from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        """
        Metadados para o formulário CarModelForm
        """

        model = Car
        fields = "__all__"

        def __init__(self):
            self.cleaned_data = None

        def clean_value(self):
            """
            Validação de campos personalizados
            """
            value = self.cleaned_data.get("value")
            if value < 20000:
                raise forms.ValidationError("Valor mínimo de R$ 20.000,00.")
            return value
