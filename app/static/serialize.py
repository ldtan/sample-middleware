# class Serializer(object):

#     def __init__(self, **kwargs):
#         cls = self.__class__

#         if len(kwargs) > 0:
#             if not cls.validate_format(kwargs):
#                 raise ValueError('Invalid parameters.')

#         else:
#             kwargs = cls.format()

#         for k, v in kwargs.iteritems():
#             exec('self.{} = v'.format(k))
    

#     @classmethod
#     def get_format(cls):
#         return {
#             k: v for k, v in cls.__dict__.iteritems()
#             if isinstance(v, type)
#         }


#     @classmethod
#     def validate_format(cls, dictionary):
#         format = cls.get_format()
#         dictionary = dict(dictionary)

#         if (dictionary == None or
#             not isinstance(dictionary, dict) or
#             len(dictionary) != len(format)):
            
#             return False

#         return all(
#             True if v == None else
#             False if not k in format else
#             format[k].validate_format(v) if issubclass(format[k], DictionaryFormatter) else
#             isinstance(v, format[k])
#             for k, v in dictionary.iteritems()
#         )


#     @classmethod
#     def format(cls, **kwargs):
#         if len(kwargs) < 1:
#             return {k: None for k in cls.get_format()}

#         if not cls.validate_format(dict(kwargs)):
#             raise ValueError('Invalid format.')

#         return dict(kwargs)



# class StatusSerializer(Serializer):

#     code = int
#     title = str
#     detail = str



# class ContentSerializer(Serializer):

#     status = StatusSerializer
#     resource = str
#     body = object



class AttributeType(dict):
    
    def __init__(self, name=None, data_type=object, default=None, nullable=True):
        if not (isinstance(name, str) and len(name) > 0):
            raise ValueError("Invalid '{}' as a 'name'.".format(str(name)))
        
        if isinstance(data_type, list):
            if any(not isinstance(t, type) for t in data_type):
                raise ValueError("Invalid {} as a 'data_type'.".format(str(data_type)))

            if any(not isinstance(default, t) for t in data_type):
                raise ValueError("Parameter 'default' can be type {}.".format(str(data_type)))
        
        else isinstance(data_type, type):
            if not isinstance(data_type, type):
                raise ValueError("Invalid '{}' as a 'data_type'.".format(str(data_type)))

            if not isinstance(default, data_type):
                raise ValueError("Parameter 'default' must be type '{}'.".format(data_type.__name__))

        if not isinstance(nullable, bool):
            raise ValueError("Parameter 'nullable' must be type 'bool'.")

        self['name'] = name
        self['data_type'] = data_type
        self['default'] = default
        self['nullable'] = nullable



class AttributeReference(dict):
    
    def __init__(self, ):
        

class Serializer(object):
    pass



# Main
print AttributeType()