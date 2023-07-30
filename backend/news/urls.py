from django.urls import path
from .views import News, New, NewLike, NewDisLike, NewComments

urlpatterns = [
    path('<int:blog_id>', News.as_view()),
    path('notice/<int:notice_id>', New.as_view()),
    path('notice/<int:notice_id>/like', NewLike.as_view()), 
    path('notice/<int:notice_id>/dislike', NewDisLike.as_view()),
    path('notice/<int:notice_id>/comments', NewComments.as_view()), 
]
