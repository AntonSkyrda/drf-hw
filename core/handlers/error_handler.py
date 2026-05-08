from rest_framework.response import Response
from rest_framework.views import exception_handler


def error_handler(exception: Exception, context: dict):
    handlers = {
        "JWTException": _jwt_validation_exception_handler,
    }

    response = exception_handler(exception, context)
    ext_class = exception.__class__.__name__

    if ext_class in handlers:
        return handlers[ext_class](exception, context)

    return response


def _jwt_validation_exception_handler(exception: Exception, context: dict):
    return Response({"detail": "JWT expired or invalid"}, status=400)
