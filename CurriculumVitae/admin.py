from django.contrib import admin
from .models import ContactInfo, SocialLinks, CurriculumVitae, Skills, Interests, WorkExperience, Education

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'direccion')

class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url', 'contact_info')

class CurriculumVitaeAdmin(admin.ModelAdmin):
    list_display = ('user', 'description')

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'assessment', 'curriculum')

class InterestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'curriculum')

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'range', 'curriculum')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('nameinst', 'title', 'range', 'curse', 'curriculum')

# Registra tus modelos con sus correspondientes clases de administrador
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)
admin.site.register(CurriculumVitae, CurriculumVitaeAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Interests, InterestsAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Education, EducationAdmin)
