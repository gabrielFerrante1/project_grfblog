from rest_framework.views import APIView, Response, status
from .serializers import BlogSerializer, BlogsSerializer, BlogWarningSerializer, BlogAreasSerializer, BlogVisibleAreasSerializer, BlogVisibleAreaSerializer

from .models import Blog as ModelBlog, Warning, Area, Visible_Area

from rest_framework.pagination import PageNumberPagination
from .utils.exceptions import NotFoundBlog,NotFoundWarning
from .utils.permissions import BlogsPermission

class Blog(APIView):
    permission_classes = [BlogsPermission]
    paginator = PageNumberPagination()

    def get(self, request):
        blogs = ModelBlog.objects.filter(user_id=request.user.id)
        paginate_queryset = self.paginator.paginate_queryset(blogs, request)

        serializer = BlogsSerializer(paginate_queryset, many=True)
        data = self.paginator.get_paginated_response(serializer.data).data

        return Response(data)

    def post(self, request):
        blog = BlogSerializer(data=request.data)

        if blog.is_valid():
            blog.save(user_id=request.user.id)
            return Response(blog.data, status=status.HTTP_201_CREATED)

        return Response({'errors': blog.errors})

    def put(self, request, blog_id):
        blog = get_blog(blog_id, request.user.id)

        serializer = BlogSerializer(blog, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.update(instance=blog,
                              validated_data=request.data)
            return Response({'errors':  serializer.data})

        return Response({'blog':  serializer.errors})

    def delete(self, request, blog_id):
        blog = get_blog(blog_id, request.user.id)

        blog.delete()

        return Response({'error':  ''})


class BlogsWarnings(APIView):
    permission_classes = [BlogsPermission]

    def get(self, request, blog_id):
        get_blog(blog_id, request.user.id)

        warnings = Warning.objects.filter(blog_id=blog_id)

        serializer = BlogWarningSerializer(warnings, many=True)

        return Response({'warnings': serializer.data})

    def post(self, request, blog_id):
        blog = get_blog(blog_id, request.user.id)

        serializer = BlogWarningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog_id=blog.id)
            return Response({'warning': serializer.validated_data})

        return Response({'errors': serializer.errors}) 

class BlogWarning(APIView):
    permission_classes = [BlogsPermission]

    def put(self, request, blog_id, warning_id):
        get_blog(blog_id, request.user.id)

        warning = get_warning(warning_id)

        serializer = BlogWarningSerializer(warning, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(warning, serializer.validated_data)

        return Response({'warning': serializer.data})

    def delete(self, request, blog_id, warning_id):
        get_blog(blog_id, request.user.id)

        warning = get_warning(warning_id)

        serializer = BlogWarningSerializer(warning)

        warning.delete()
        return Response({'warning': serializer.data})

class BlogAreas(APIView):
    def get(self, request):
        areas = Area.objects.all()

        serializer = BlogAreasSerializer(areas, many=True)

        return Response({'areas': serializer.data})

class BlogVisibleAreas(APIView):
    def get(self, request, blog_id):
        blog = get_blog(blog_id, request.user.id)

        visible_areas = Visible_Area.objects.filter(blog_id=blog.id)

        serializer = BlogVisibleAreasSerializer(visible_areas, many=True)

        return Response({'areas':serializer.data})


class BlogVisibleArea(APIView):
    permission_classes = [BlogsPermission]
    def put(self, request, blog_id, area_id):
        blog = get_blog(blog_id, request.user.id)
    
        area_visibilty = Visible_Area.objects.filter(area_id=area_id, blog_id=blog.id).first()
        if area_visibilty: 
            Visible_Area.objects.filter(area_id=area_id, blog_id=blog.id).update(visible= request.POST.get('visible') or 1 - area_visibilty.visible )
        else: 
            serializer = BlogVisibleAreaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(blog_id=blog_id, area_id=area_id)
                return Response({'visibility_area':serializer.data})
            else:
                return Response({'areas':serializer.errors})
        
        area_visibilty = Visible_Area.objects.filter(area_id=area_id, blog_id=blog_id).first()
        area_visibilty_serializer = BlogVisibleAreaSerializer(area_visibilty)
        
        return Response({'visibility_area':area_visibilty_serializer.data})


# Funções que são usadas em quase todas as classes
def get_blog(blog_id: int, user_id: int):
    blog = ModelBlog.objects.filter(
         id=blog_id, user_id=user_id).first()
    if not blog:
        raise NotFoundBlog

    return blog

def get_warning(warning_id: int):
    warning = Warning.objects.filter(
        id=warning_id).first()
    if not warning:
        raise NotFoundWarning

    return warning