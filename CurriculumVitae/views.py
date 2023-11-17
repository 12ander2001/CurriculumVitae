from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import SocialLinks, ContactInfo, Skills, Interests, WorkExperience, Education, CurriculumVitae
from .serializers import SocialLinksSerializer, ContactInfoSerializer, SkillsSerializer, InterestsSerializer, WorkExperienceSerializer, EducationSerializer, CurriculumVitaeSerializer
from django.contrib.auth import get_user_model
from .permissions import CanCreateSkills, CanCreateEducation, CanCreateInterests, CanCreateWorkExperience, CanCreateSocialLinks, CanCreateContactInfo, CanCreateCurriculumVitae

class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer
    permission_classes = [CanCreateSocialLinks]
    
class ContactInfoViewSet(viewsets.ModelViewSet):
   queryset = ContactInfo.objects.all()
   serializer_class = ContactInfoSerializer
   permission_classes = [CanCreateContactInfo]
    
   def create(self, request, *args, **kwargs):
    user = request.user
    data = request.data
    serializer = self.get_serializer(data=data)
    serializer.is_valid(raise_exception=True)
    contact_info = serializer.save(user=user)
    return Response({'id': contact_info.id, 'data': serializer.data}, status=status.HTTP_201_CREATED)

    def get_queryset(self):
       user = self.request.user
       return ContactInfo.objects.filter(user=user)

   def update(self, request, *args, **kwargs):
       instance = self.get_object()
       if request.user != instance.user:
           return Response(status=status.HTTP_403_FORBIDDEN)
       serializer = self.get_serializer(instance, data=request.data)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       return Response(serializer.data)

   def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       if request.user != instance.user:
           return Response(status=status.HTTP_403_FORBIDDEN)
       self.perform_destroy(instance)
       return Response(status=status.HTTP_204_NO_CONTENT)

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [CanCreateSkills]

class InterestsViewSet(viewsets.ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
    permission_classes = [CanCreateInterests]

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [CanCreateWorkExperience]
      
class EducationViewSet(viewsets.ModelViewSet):
   queryset = Education.objects.all()
   serializer_class = EducationSerializer
   permission_classes = [CanCreateEducation]
   
   def perform_create(self, serializer):
       instance = serializer.save()
       instance_id = instance.id
       # Aquí puedo hacer lo que quieras con instance_id
       return Response({"message": "Datos guardados", "Id": instance_id}, status=status.HTTP_201_CREATED)


CustomUser = get_user_model()

class CurriculumVitaeViewSet(viewsets.ModelViewSet):
   queryset = CurriculumVitae.objects.all()
   serializer_class = CurriculumVitaeSerializer
   permission_classes = [CanCreateCurriculumVitae]

   def create(self, request, *args, **kwargs):
    user = request.user
    data = request.data
    serializer = self.get_serializer(data=data)
    serializer.is_valid(raise_exception=True)
    curriculum_vitae = serializer.save(user=user)
    return Response({'id': curriculum_vitae.id, 'data': serializer.data}, status=status.HTTP_201_CREATED)


   def get_queryset(self):
       user = self.request.user
       return CurriculumVitae.objects.filter(user=user)

   def update(self, request, *args, **kwargs):
       instance = self.get_object()
       if request.user != instance.user:
           return Response(status=status.HTTP_403_FORBIDDEN)
       serializer = self.get_serializer(instance, data=request.data)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       return Response(serializer.data)

   def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       if request.user != instance.user:
           return Response(status=status.HTTP_403_FORBIDDEN)
       self.perform_destroy(instance)
       return Response(status=status.HTTP_204_NO_CONTENT)