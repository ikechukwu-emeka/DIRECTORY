from django.forms import ModelForm
from .models import Telephone


class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone
        fields = ['forename', 'surname','middle_name','phone_number','gender']