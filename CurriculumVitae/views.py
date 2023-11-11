from rest_framework import viewsets
from .models import SocialLinks, ContactInfo, Skills, Interests, WorkExperience, Education, CurriculumVitae
from .serializers import SocialLinksSerializer, ContactInfoSerializer, SkillsSerializer, InterestsSerializer, WorkExperienceSerializer, EducationSerializer, CurriculumVitaeSerializer

class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer

class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class InterestsViewSet(viewsets.ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer
