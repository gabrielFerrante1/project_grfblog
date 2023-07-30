from rest_framework import serializers
from .models import Blog, Warning, Area, Visible_Area


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'title', 
            'color_primary',
            'color_secondary'
        )

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'description',
            'color_primary',
            'color_secondary'
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.color_primary = validated_data.get('color_primary', instance.color_primary)
        instance.color_secondary = validated_data.get('color_secondary', instance.color_secondary)

        instance.save()
        return instance

class BlogWarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = (
            'title',
            'txtcolor',
            'bgcolor',
        )


class BlogAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ( 
            'name',
        )


class BlogVisibleAreasSerializer(serializers.ModelSerializer): 
    area = serializers.SerializerMethodField()

    class Meta:
        model = Visible_Area
        fields = (
            'id',
            'visible',
            'area',
        )

    def get_area(self, obj): 
        return Area.objects.filter(id=obj.id).first().name


class BlogVisibleAreaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Visible_Area
        fields = (
            'id',
            'visible', 
        ) 