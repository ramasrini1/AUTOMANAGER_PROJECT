from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'street', 'city', 'state1', 'zipcode', 
                  'mobile', 'email', 'make', 'model', 'series',
                 'vin', 'lic', 'state', 'memo' ]

