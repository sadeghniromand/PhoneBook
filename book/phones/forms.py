from django import forms
from .models import PhoneBook


class CreatPhone(forms.ModelForm):

    class Meta:
        model = PhoneBook
        fields = (
            "name",
            "last",
            "phone_number",
        )
