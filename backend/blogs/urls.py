from django.urls import include, path
from .views import Blog, BlogWarning, BlogsWarnings, BlogAreas, BlogVisibleAreas, BlogVisibleArea

urlpatterns = [
    path('', Blog.as_view()),
    path('<int:blog_id>', Blog.as_view()),
    path('<int:blog_id>/warnings', BlogsWarnings.as_view()),
    path('<int:blog_id>/warnings/<int:warning_id>', BlogWarning.as_view()), 
    path('areas', BlogAreas.as_view()), 
    path('<int:blog_id>/areas/visibility', BlogVisibleAreas.as_view()), 
    path('<int:blog_id>/areas/visibility/<int:area_id>', BlogVisibleArea.as_view()), 
]
