CLASS = 'cls'
OBJECT = 'self'


class Serializer(object):
    
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            try:
                for k, v in args[0].__dict__.iteritems():
                    if callable(v) or k[0:2] == '__':
                        continue

                    try:
                        v = Serializer(v)

                    except:
                        v = v

                    exec('self.{} = v'.format(k))

            except AttributeError as e:
                pass

        elif len(kwargs) > 1:
            for k, v in kwargs.iteritems():
                exec('self.{} = v'.format(k))
    
    
    def __getVariables__(self, instance):
        variables = {}

        if OBJECT in instance:
            variables.update({
                k: v for k, v in self.__dict__.iteritems()
                if not callable(v) and not k[0:2] == '__'
            })

        if CLASS in instance:
            variables.update({
                'class_' + k if k in variables else k:
                v for k, v in self.__class__.__dict__.iteritems()
                if not callable(v) and not k[0:2] == '__'
            })

        return variables


    def serialize(self, instance=[OBJECT, CLASS], include=None, exclude=None):
        return {
            k: v.serialize() if isinstance(v, Serializer) else v
            for k, v in self.__getVariables__(instance).iteritems()
            if not include and not exclude or
            not exclude and k in include or
            not include and not k in exclude
        }


# Main
class Sample(Serializer, list):

    id = 100
    
    def __init__(self):
        super(self.__class__, self).__init__(data=None)
        self.id = 0
        self.name = 'Liel'
        self.serial = Serializer(age=20, city='Quezon City')


# s = Sample()
# print s.__dict__
# print isinstance(long, object)

# for k, v in s.serialize().iteritems():
#     print k, '=', v

'''
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


class AttributeDefiniton(dict):
    
    def serialize(self):
        raise NotImplementedError('Function not yet implemented.')


# class AttributeType(AttributeDefiniton):
    
#     def __init__(self, name=None, data_type=object, default=None, nullable=True):
#         if not (isinstance(name, str) and len(name) > 0):
#             raise ValueError("Invalid '{}' as a 'name'.".format(str(name)))
        
#         if isinstance(data_type, list):
#             if any(not isinstance(t, type) for t in data_type):
#                 raise ValueError("Invalid {} as a 'data_type'.".format(str(data_type)))

#             if any(not isinstance(default, t) for t in data_type):
#                 raise ValueError("Parameter 'default' can be type {}.".format(str(data_type)))
        
#         else:
#             if not isinstance(data_type, type):
#                 raise ValueError("Invalid '{}' as a 'data_type'.".format(str(data_type)))

#             if not isinstance(default, data_type):
#                 raise ValueError("Parameter 'default' must be type '{}'.".format(data_type.__name__))

#         if not isinstance(nullable, bool):
#             raise ValueError("Parameter 'nullable' must be type 'bool'.")

#         self['name'] = name
#         self['data_type'] = data_type
#         self['default'] = default
#         self['nullable'] = nullable
        
#         cls = self.__class__
#         __readonly__ = self.__readonly__
#         cls.__setitem__ = __readonly__
#         cls.__delitem__ = __readonly__
#         cls.pop = __readonly__
#         cls.popitem = __readonly__
#         cls.clear = __readonly__
#         cls.update = __readonly__
#         cls.setdefault = __readonly__
#         del __readonly__

    
#     def __readonly__(self, *args, **kwargs):
#         raise RuntimeError("Cannot modify read-only 'dict'.")

CLASS = 'cls'
OBJECT = 'self'



class AttributeReference(AttributeDefiniton):
    
    def __init__(self, reference_name=None, instance=OBJECT, data_type=object, default=None, nullable=True, convert=None):
        if not instance in [CLASS, OBJECT]:
            raise ValueError("Invalid '{}' as 'instance'.".format(str(instance)))
        
        if isinstance(data_type, list):
            if any(not isinstance(t, type) for t in data_type):
                raise ValueError("Invalid {} as a 'data_type'.".format(str(data_type)))

            if default and any(not isinstance(default, t) for t in data_type):
                raise ValueError("Parameter 'default' can be type {}.".format(str(data_type)))
        
        else:
            if not isinstance(data_type, type):
                raise ValueError("Invalid '{}' as a 'data_type'.".format(str(data_type)))

            if default and not isinstance(default, data_type):
                raise ValueError("Parameter 'default' must be type '{}'.".format(data_type.__name__))

        if not isinstance(nullable, bool):
            raise ValueError("Parameter 'nullable' must be type 'bool'.")

        not_implemented = self.not_implemented
        
        if convert and not callable(convert):
            raise ValueError("Parameter 'convert' must be a function.")

        self['reference_name'] = reference_name
        self['instance'] = instance
        self['data_type'] = data_type
        self['default'] = default
        self['nullable'] = nullable
        self['convert'] = convert if convert else not_implemented
        del not_implemented


    def not_implemented(self, *args, **kwargs):
        raise NotImplementedError('Conversion is not implemented.')
        


class Serializer(object):
    
    def __getAttributeDefinitions__(self):
        return {
            k: v for k, v in self.__class__.__dict__.iteritems()
            if isinstance(v, AttributeDefiniton)
        }


    def serialize(self):
        cls = self.__class__
        definitions = self.__getAttributeDefinitions__()
        serialized = {}

        for k, v in definitions.iteritems():
            k = v['reference_name'] if v['reference_name'] else k
            value = None

            if not v['instance'] in [CLASS, OBJECT]:
                raise ValueError("Invalid instance.")
            
            if eval('k in {}.__dict__'.format(v['instance'])):
                value = eval('{}.{}'.format(v['instance'], k))

            else:
                raise NameError("'reference_name' is not defined.")

            value = value if value else v['default']

            if not value and not v['nullable']:
                raise ValueError("'{}' must have a value.".format(k))

            if isinstance(value, Serializer):
                value = value.serialize()
            
            elif (not any(isinstance(value, d) for k, v in v['data_type'])
                  if isinstance(v['data_type'], list) else
                  not isinstance(value, v['data_type'])
                  if isinstance(v['data_type'], type) else
                  False):
                
                convert = v['convert']
                value = convert(value=value, data_type=v['data_type'])

            serialized.update({k: value})

        return serialized



class ClassSerializer(Serializer):

    def __getAttributeDefinitions__(self):
        return self.__class__.__dict__


    def serialize(self):
        cls = self.__class__
        variables = self.__getAttributeDefinitions__()
        serialized = {}

        for k, v in variables.iteritems():
            if callable(v):
                continue

            value = eval('cls.{}'.format(k))
            value = (value.serialize() if isinstance(value, Serializer)
                     else value)

            serialized.update({k: value})


def converter(value=None, data_type=str):
    return str(value)


class Sample(Serializer):

    id = AttributeReference(
        instance=OBJECT
    )

    def __init__(self):
        self.id = 1


print Sample().serialize()'''