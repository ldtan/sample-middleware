class Serializer(object):

    def __init__(self, **kwargs):
        cls = self.__class__

        if len(kwargs) > 0:
            if not cls.validate_format(kwargs):
                raise ValueError('Invalid parameters.')

        else:
            kwargs = cls.format()

        for k, v in kwargs.iteritems():
            exec('self.{} = v'.format(k))
    

    @classmethod
    def get_format(cls):
        return {
            k: v for k, v in cls.__dict__.iteritems()
            if isinstance(v, type)
        }


    @classmethod
    def validate_format(cls, dictionary):
        format = cls.get_format()
        dictionary = dict(dictionary)

        if (dictionary == None or
            not isinstance(dictionary, dict) or
            len(dictionary) != len(format)):
            
            return False

        return all(
            True if v == None else
            False if not k in format else
            format[k].validate_format(v) if issubclass(format[k], DictionaryFormatter) else
            isinstance(v, format[k])
            for k, v in dictionary.iteritems()
        )


    @classmethod
    def format(cls, **kwargs):
        if len(kwargs) < 1:
            return {k: None for k in cls.get_format()}

        if not cls.validate_format(dict(kwargs)):
            raise ValueError('Invalid format.')

        return dict(kwargs)



class StatusSerializer(Serializer):

    code = int
    title = str
    detail = str



class ContentSerializer(Serializer):

    status = StatusSerializer
    resource = str
    body = object