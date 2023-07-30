from rest_framework import permissions 

class BlogsPermission(permissions.BasePermission): 
    SAFE_METHODS = ['GET']

    def has_permission(self, request, view):
        if request.method in self.SAFE_METHODS:
            return True

        if request.user.is_authenticated: 
            return request.user.groups.filter(name__in=['Administrador', 'Editor do blog']).exists()