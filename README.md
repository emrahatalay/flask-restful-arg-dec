# flask-restful-arg-dec
Decorator based argument parser for flask-restful

```python
from flask import Flask
from flask_restful import Api, Resource
from frad import ArgumentAdder, RequestParser

...

class RegisterResource(Resource):
  @ArgumentAdder('username', type=str, help='Username field cannot be blank!', required=True)
  @ArgumentAdder('password')
  @RequestParser
  def post(self, **kw):
    data = kw.get('data')
    print("username: {username}, password: {password}".format(**data))
    
    
...
    
```
