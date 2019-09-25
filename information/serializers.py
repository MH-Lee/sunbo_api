from rest_framework import serializers
from .models import (
    CompanyCode, EM01,
    AA22, AA06, AB01,
    AB09, AD01, AZ06
    )


class CompanyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCode
        fields = '__all__'


class EM01Serializer(serializers.ModelSerializer):
    class Meta:
        model = EM01
        fields = '__all__'

class AA22Serializer(serializers.ModelSerializer):
    class Meta:
        model = AA22
        fields = '__all__'


class AA06Serializer(serializers.ModelSerializer):
    class Meta:
        model = AA06
        fields = '__all__'


class AB01Serializer(serializers.ModelSerializer):
    rep_name = serializers.CharField(source='get_rep_code_display')
    class Meta:
        model = AB01
        fields = '__all__'


class AB09Serializer(serializers.ModelSerializer):
    class Meta:
        model = AB09
        fields = '__all__'


class AD01Serializer(serializers.ModelSerializer):
    rep_name = serializers.CharField(source='get_rep_code_display')
    class Meta:
        model = AD01
        fields = '__all__'


class AZ06Serializer(serializers.ModelSerializer):
    cr_name = serializers.CharField(source='get_cr_code_display')
    class Meta:
        model = AZ06
        fields = '__all__'
