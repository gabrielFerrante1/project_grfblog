from rest_framework.exceptions import APIException

class NotFoundBlog(APIException):
    status_code = 404
    default_detail = 'O blog não pode ser encontrada'
    default_code = 'not_found_blog'
    
class NotFoundWarning(APIException):
    status_code = 404
    default_detail = 'O alerta não pode ser encontrada'
    default_code = 'not_found_warning'