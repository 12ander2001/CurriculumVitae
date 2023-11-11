from django.db import models
from User.models import CustomUser
from rest_framework import viewsets


class SocialLinks(models.Model):
    nombre = models.CharField(max_length=255)
    url = models.URLField()

def get_default_user():
    user = CustomUser.objects.first() 
    return user

class ContactInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=get_default_user)
    phone = models.CharField(max_length=15)
    sociallinks = models.ForeignKey(SocialLinks, on_delete=models.CASCADE)
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


class Skills(models.Model):
    name = models.CharField(max_length=255)
    assessment = models.CharField(max_length=255)

class Interests(models.Model):
    name = models.CharField(max_length=255)

class WorkExperience(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    description = models.TextField()

class Education(models.Model):
    nameinst = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    curse = models.CharField(max_length=255)
    description = models.TextField()

class CurriculumVitae(models.Model):
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True, editable=False)
    interest = models.ForeignKey(Interests, on_delete=models.CASCADE)
    description = models.TextField()
    workexperience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

