from django.db import models
from User.models import CustomUser
from rest_framework import viewsets

def get_default_user():
    user = CustomUser.objects.first()
    if user:
        return user.id
    return None  # o el valor que desees usar si no hay usuarios


class ContactInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=get_default_user)
    phone = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    
    @property
    def user_email(self):
        return self.user.email
    
    @property
    def user_username(self):
        return self.user.username
    
    @property
    def user_firstname(self):
        return self.user.firstname
    
    @property
    def user_lastname(self):
        return self.user.lastname
    
class SocialLinks(models.Model):
    nombre = models.CharField(max_length=255)
    url = models.URLField()
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, related_name='social_links')
    
    
class CurriculumVitae(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True, editable=False)
    description = models.TextField()
    
    def __str__(self):
        return self.user.username


class Skills(models.Model):
    name = models.CharField(max_length=255)
    assessment = models.CharField(max_length=255)
    curriculum = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE, related_name='skills')



class Interests(models.Model):
    name = models.CharField(max_length=255)
    curriculum = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE, related_name='interests')


class WorkExperience(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    description = models.TextField()
    curriculum = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE, related_name='workexperience')


class Education(models.Model):
    nameinst = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    curse = models.CharField(max_length=255)
    description = models.TextField()
    curriculum = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE, related_name='educations')


