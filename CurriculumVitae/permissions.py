from rest_framework import permissions

class CanCreateSkills(permissions.BasePermission):
  def has_permission(self, request, view):
      return request.method in permissions.SAFE_METHODS or request.user.is_authenticated

class CanCreateWorkExperience(permissions.BasePermission):
  def has_permission(self, request, view):
      return request.method in permissions.SAFE_METHODS or request.user.is_authenticated
  
class CanCreateEducation(permissions.BasePermission):
  def has_permission(self, request, view):
      return request.method in permissions.SAFE_METHODS or request.user.is_authenticated  
  
class CanCreateInterests(permissions.BasePermission):
  def has_permission(self, request, view):
      return request.method in permissions.SAFE_METHODS or request.user.is_authenticated

class CanCreateSocialLinks(permissions.BasePermission):
  def has_permission(self, request, view):
      return request.method in permissions.SAFE_METHODS or request.user.is_authenticated
  
class CanCreateContactInfo(permissions.BasePermission):
  def has_permission(self, request, view):
      return request.method in permissions.SAFE_METHODS or request.user.is_authenticated
  
class CanCreateCurriculumVitae(permissions.BasePermission):
  def has_permission(self, request, view):
      return request.method in permissions.SAFE_METHODS or request.user.is_authenticated