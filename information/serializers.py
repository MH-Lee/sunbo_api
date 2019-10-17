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
    com_name = serializers.SerializerMethodField('get_com_name')
    market_code = serializers.SerializerMethodField('get_mk_code')
    class Meta:
        model = EM01
        fields = '__all__'
    
    def get_com_name(self, obj):
        return obj.com_code.com_name
    
    def get_mk_code(self, obj):
        return obj.com_code.market_code

class AA22Serializer(serializers.ModelSerializer):
    com_name = serializers.SerializerMethodField('get_com_name')
    class Meta:
        model = AA22
        fields = '__all__'
    
    def get_com_name(self, obj):
        return obj.com_code.com_name


class AA06Serializer(serializers.ModelSerializer):
    com_name = serializers.SerializerMethodField('get_com_name')

    class Meta:
        model = AA06
        fields = '__all__'
    
    def get_com_name(self, obj):
        return obj.com_code.com_name

class AB01Serializer(serializers.ModelSerializer):
    rep_name = serializers.CharField(source='get_rep_code_display')
    class Meta:
        model = AB01
        fields = '__all__'


class AB09Serializer(serializers.ModelSerializer):
    rep_name = serializers.CharField(source='get_rep_code_display')
    class Meta:
        model = AB09
        fields = '__all__'


class AD01Serializer(serializers.ModelSerializer):
    rep_name = serializers.CharField(source='get_rep_code_display')
    class Meta:
        model = AD01
        fields = '__all__'


class AZ06Serializer(serializers.ModelSerializer):
    com_name = serializers.SerializerMethodField('get_com_name')
    cr_name = serializers.CharField(source='get_cr_code_display')
    class Meta:
        model = AZ06
        fields = '__all__'
    
    def get_com_name(self, obj):
        return obj.com_code.com_name