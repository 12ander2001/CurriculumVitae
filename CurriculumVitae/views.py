from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import SocialLinks, ContactInfo, Skills, Interests, WorkExperience, Education, CurriculumVitae
from .serializers import SocialLinksSerializer, ContactInfoSerializer, SkillsSerializer, InterestsSerializer, WorkExperienceSerializer, EducationSerializer, CurriculumVitaeSerializer
from django.contrib.auth import get_user_model

class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer
    permission = "__all__"

class ContactInfoViewSet(viewsets.ModelViewSet):
   queryset = ContactInfo.objects.all()
   serializer_class = ContactInfoSerializer
   permission = "__all__"
    
   def create(self, request, *args, **kwargs):
    user = request.user
    data = request.data
    serializer = self.get_serializer(data=data)
    serializer.is_valid(raise_exception=True)
    contact_info = serializer.save(user=user)
    return Response({'id': contact_info.id, 'data': serializer.data}, status=status.HTTP_201_CREATED)

   def update(self, request, *args, **kwargs):
    instance = self.get_object()
    if request.user != instance.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = self.get_serializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    return Response({'id': instance.id, 'data': serializer.data}, status=status.HTTP_200_OK)

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission = "__all__"

class InterestsViewSet(viewsets.ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
    permission = "__all__"

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission = "__all__"
      
class EducationViewSet(viewsets.ModelViewSet):
   queryset = Education.objects.all()
   serializer_class = EducationSerializer
   permission = "__all__"

CustomUser = get_user_model()

class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer
    permission = "__all__"

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        curriculum_vitae = serializer.save(user=user)
        return Response({'id': curriculum_vitae.id, 'data': serializer.data}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'id': instance.id, 'data': serializer.data}, status=status.HTTP_200_OK)
