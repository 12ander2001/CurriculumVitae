from rest_framework import serializers
from .models import CustomUser
from CurriculumVitae.serializers import CurriculumVitaeSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    curriculum = CurriculumVitaeSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'firstname', 'lastname', 'curriculum']
