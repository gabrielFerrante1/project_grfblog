from rest_framework.serializers import *
from .models import Notice, Comment

class NoticesSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            'id',
            'title',
            'subtitle',
            'body',
            'date',
        )

class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'title',
            'body',
            'date', 
        )