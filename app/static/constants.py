from serialize import Serializer


MICROSERVICE_URL = 'http://10.237.158.163:8080'
MIDDLEWARE_URL = 'http://10.237.159.108:8081'

PRIMITIVE_TYPES = (
    bool,
    int, long, float, complex,
    str, bytes, bytearray,
    list, tuple, set,
    dict
)

REQUEST_METHODS = (
    'POST',
    'GET',
    'PUT',
    'DELETE',
    'OPTION'
)