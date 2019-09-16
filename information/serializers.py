from rest_framework import serializers
from .models import (
    em01, aa22, aa06,
    ab01, ab09, ad01,
    az06
    )

class em01Serializer(serializers.ModelSerializer):
    class Meta:
        model = em01
        fields = '__all__'

class aa22Serializer(serializers.ModelSerializer):
    class Meta:
        model = aa22
        fields = '__all__'


class aa06Serializer(serializers.ModelSerializer):
    class Meta:
        model = aa06
        fields = '__all__'


class ab01Serializer(serializers.ModelSerializer):
    class Meta:
        model = ab01
        fields = '__all__'


class ab09Serializer(serializers.ModelSerializer):
    class Meta:
        model = ab09
        fields = '__all__'


class ad01Serializer(serializers.ModelSerializer):
    class Meta:
        model = ad01
        fields = '__all__'


class az06Serializer(serializers.ModelSerializer):
    class Meta:
        model = az06
        fields = '__all__'
