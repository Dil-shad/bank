from rest_framework.serializers import ModelSerializer
from myapp.models import BankDetail
from rest_framework import serializers
from django.contrib.auth.models import User
class BankSerializer(ModelSerializer):
    class Meta:
        model=BankDetail
        fields='__all__'


