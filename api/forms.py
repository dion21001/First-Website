from django import forms

from .models import CoffeeOrder


class CoffeeOrderForm(forms.ModelForm):
    class Meta:
        model = CoffeeOrder
        fields = [
            "coffee",
            "customer_name",
            "phone_number",
            "address",
            "quantity",
            "grind_size",
            "notes",
        ]
        widgets = {
            "coffee": forms.Select(),
            "customer_name": forms.TextInput(
                attrs={"placeholder": "Nama lengkap"}
            ),
            "phone_number": forms.TextInput(
                attrs={"placeholder": "08xxxxxxxxxx"}
            ),
            "address": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Alamat pengiriman"}
            ),
            "quantity": forms.NumberInput(attrs={"min": 1}),
            "grind_size": forms.Select(),
            "notes": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Catatan tambahan (opsional)"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "order-input")
