from rest_framework import serializers
from .models import Pizzeria


class PizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'city',
            'street',
            'zip_code',
            'email',
            'website',

        ]


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'street',
            'city',
            'state',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active',

        ]

