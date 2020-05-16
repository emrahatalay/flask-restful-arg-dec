from flask_restful import reqparse

class ArgumentAdder:
    def __init__(self, field, required=True, help='', type=str, **kw):        
        self.item = {'field': field, 'required': required, 'type': type}
        self.item.update(kw)
        
    def __call__(self, function):
        def wrapper(*args, arguments=[], **kw):
            arguments.append(self.item)
            value = function(*args, arguments=arguments, **kw)
            return value
        return wrapper

class RequestParser:
    def __init__(self, func):
        self.func = func
       
    def __call__(self, *args, **kwargs):
        arguments = kwargs.pop('arguments')
        parser = reqparse.RequestParser()
        for _arg in arguments:
            if "field" in _arg:
                field = _arg.pop("field")
                parser.add_argument(field, **_arg)
        data = parser.parse_args()
        return self.func(*args, data=data, **kwargs)
