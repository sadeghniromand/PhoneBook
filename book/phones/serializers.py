from rest_framework import serializers
from . import models


class PhoneSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PhoneBook
        fields = ['name', 'last', 'phone_number']


class ReadPhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneBook
        fields = ['name', 'last', 'phone_number']
