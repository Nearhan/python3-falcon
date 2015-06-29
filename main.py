import falcon
import json


class HelloWorldResourceAPI:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'application/json'
        resp.body = json.dumps({'data': 'hello world!'})

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
hello_world = HelloWorldResourceAPI()

app.add_route('/', hello_world)
