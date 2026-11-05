from django import forms


PRODUCT_CHOICES = (
    ('laptop', 'Laptop — 5,000,000 UZS'),
    ('phone', 'Phone — 3,000,000 UZS'),
    ('headphones', 'Headphones — 200,000 UZS'),
)

DELIVERY_CHOICES = (
    ('pickup', 'Pickup — Free'),
    ('courier', 'Courier — 30,000 UZS'),
)


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    product = forms.ChoiceField(choices=PRODUCT_CHOICES)
    quantity = forms.IntegerField(min_value=1)
    delivery = forms.ChoiceField(choices=DELIVERY_CHOICES)
    address = forms.CharField(
        max_length=255,
        required=False
    )
