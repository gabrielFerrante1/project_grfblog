from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        print( response.data)
        response.data['message'] = response.data['detail']
        response.data['error'] = response.data['detail'].code
        #response.data['status_code'] = response.status_code
        del response.data['detail']

    return response