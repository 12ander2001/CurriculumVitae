from rest_framework import serializers
from .models import SocialLinks, ContactInfo, CurriculumVitae, Skills, Interests, WorkExperience, Education

class ContactInfoSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    user_username = serializers.ReadOnlyField(source='user.username')
    user_firstname = serializers.ReadOnlyField(source='user.firstname')
    user_lastname = serializers.ReadOnlyField(source='user.lastname')

    class Meta:
        model = ContactInfo
        fields = ['id','user', 'phone', 'direccion', 'user_email', 'user_username', 'user_firstname', 'user_lastname']

class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'

class CurriculumVitaeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CurriculumVitae
        fields = ['user', 'description']

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
