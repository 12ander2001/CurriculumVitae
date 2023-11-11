from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialLinksViewSet, ContactInfoViewSet, SkillsViewSet, InterestsViewSet, WorkExperienceViewSet, EducationViewSet, CurriculumVitaeViewSet

router = DefaultRouter()
router.register('sociallinks', SocialLinksViewSet)
router.register('contactinfo', ContactInfoViewSet)
router.register('skills', SkillsViewSet)
router.register('interests', InterestsViewSet)
router.register('workexperience', WorkExperienceViewSet)
router.register('education', EducationViewSet)
router.register('curriculumvitae', CurriculumVitaeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
