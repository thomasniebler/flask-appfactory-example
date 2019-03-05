import flask
import views
import os


class CacheRO:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, None)

    def write(self, key, value):
        print("NOT Writing " + str(key) + " -> " + str(value))

    def get_all(self):
        return self.cache


class CacheRW(CacheRO):
    def write(self, key, value):
        print("Writing " + str(key) + " -> " + str(value))
        self.cache[key] = value


def app_factory(name, cache):
    app = flask.Flask(__name__ + "_" + str(name))
    app.register_blueprint(views.bp)
    app.config.setdefault("cache", cache)
    return app


def auto_app():
    if "DEBUG" in os.environ:
        return app_factory("debug", CacheRW())
    else:
        return app_factory("prod", CacheRO())

