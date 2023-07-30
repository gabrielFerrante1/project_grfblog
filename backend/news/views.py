from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.exceptions import APIException

from .serializers import NoticesSerializer, CommentsSerializer

from .models import Notice, Like, Dislike, Comment

from .utils.exceptions import NotFoundNotice
from .utils.permissions import NewsPermission

class News(APIView):
    permission_classes = [NewsPermission, IsAuthenticatedOrReadOnly]

    def get(self, request, blog_id):
        notices = Notice.objects.filter(blog_id=blog_id).all()
        
        serializer = NoticesSerializer(notices, many=True)

        return Response({"notices": serializer.data})

    def post(self, request, blog_id): 
        serializer = NoticesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(blog_id=blog_id, user_id=request.user.id)

            return Response({"notice": serializer.data})
        else:
            return Response({"errors": serializer.errors})

class New(APIView):
    permission_classes = [NewsPermission]

    def put(self, request, notice_id):
        notice = get_notice(notice_id)

        serializer = NoticesSerializer(notice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(instance=notice, validated_data=serializer.validated_data)

        notice = get_notice(notice_id)
        serializer = NoticesSerializer(notice)

        return Response({"notice": serializer.data})

    def delete(self, request, notice_id):
        notice = get_notice(notice_id)

        notice.delete()

        return Response({"error": ""})


class NewLike(APIView):
    def post(self, request, notice_id):
        get_notice(notice_id)

        save = Like(notice_id=notice_id)
        save.save()


class NewDisLike(APIView):
    def post(self, request, notice_id):
        get_notice(notice_id)

        save = Dislike(notice_id=notice_id)
        save.save()

class NewComments(APIView):
    permission_classes = [AllowAny]

    def get(self, request, notice_id):
        get_notice(notice_id)

        comments = Comment.objects.filter(notice_id=notice_id).all()
     
        serializer = CommentsSerializer(comments, many=True)

        return Response({"comments": serializer.data})

    def post(self, request, notice_id):
        get_notice(notice_id)

        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(notice_id=notice_id)
        else:
            detail = ''
            for key, value in serializer.errors.items():
                detail = key + ': ' + value[0]
                break

            raise APIException(detail, 'send_the_parameters_necessary')

        return Response({"comment": serializer.data})

# Function ulizadas em varias classes
def get_notice(notice_id):
    notice = Notice.objects.filter(id=notice_id).first()

    if not notice:
        raise NotFoundNotice
    
    return notice
