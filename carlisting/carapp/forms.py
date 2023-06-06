from datetime import date, timezone
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Car
from django.core.validators import RegexValidator


class CarForm(forms.ModelForm):
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Mobile number must be entered in the format: '+999999999'. only 10 digits allowed."
    )

    seller_mobile = forms.CharField(
        max_length=15,
        validators=[mobile_regex]
    )
    class Meta:
        model = Car
        fields = ['seller_name', 'seller_mobile', 'make', 'model', 'year', 'condition', 'asking_price']
        widgets = {
            'year':  forms.SelectDateWidget(years=range(date.today().year - 50, date.today().year + 1)),
            'asking_price': forms.TextInput(attrs={'type': 'number', 'min': 1000, 'max': 100000}),
        }
    
    

    def clean_asking_price(self):
        asking_price = self.cleaned_data.get('asking_price')
        if asking_price < 1000 or asking_price > 100000:
            raise forms.ValidationError("Invalid asking price. Must be between $1,000 and $100,000.")
        return asking_price


class BuyForm(forms.Form):
    buyer_name = forms.CharField(label='Your Name', max_length=100)
    buyer_mobile = forms.CharField(label='Your Mobile Number', max_length=15)
