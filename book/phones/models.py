from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
phone_regex = RegexValidator(regex='^09[0-9]{9}$',
                             message="Phone number must be entered in the format: '0999999999'. Up to 11 digits allowed.")


# /^09[0-9]{9}$/gm

class PhoneBook(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_("user"))
    name = models.CharField(max_length=60, verbose_name=_("first name"))
    last = models.CharField(max_length=60, verbose_name=_("last name"))
    phone_number = models.CharField(validators=[phone_regex], max_length=11, verbose_name=_("phone number"))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'phone_number'], name='user_num')
        ]

    def __str__(self):
        return f"phone number for {self.user}"

