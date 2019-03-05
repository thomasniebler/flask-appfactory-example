# flask-appfactory-example
An example of a customizable app factory for flask, depending on environment variables.
This example is losely similar to http://flask.pocoo.org/docs/1.0/patterns/appfactories/.

The main gist of this example is that we start the flask app using gunicorn as follows:

```bash
gunicorn "main:auto_app()"
```

Using `auto_app()`, we are able to set up different configurations of a flask app object.
To use the same routing implementations, we make use of [Flask Blueprints](http://www.google.com)
(see `views.py`).
For example, we could start the server with debug settings or a different cache implementation.

In this concrete implementation, when starting up gunicorn with an environment variable `RWCACHE`,
we can use `<yourserver>/write/<key>/<value>` to save `{key: value}` in the app's cache:

```bash
RWCACHE=1 gunicorn "main:auto_app()" 
```

When ommitting `RWCACHE`, the cache is ready-only.
While this is obviously an example without a real use case, it perfectly depicts how to use
different app configurations.

