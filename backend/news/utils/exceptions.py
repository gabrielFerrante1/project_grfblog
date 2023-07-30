from rest_framework.exceptions import APIException

class NotFoundNotice(APIException):
    status_code = 404
    default_detail = 'A notícia não pode ser encontrada'
    default_code = 'not_found_notice'