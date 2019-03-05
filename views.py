import flask

bp = flask.Blueprint("views_bp", __name__)

@bp.route("/", methods=["GET"])
def get_all():
    return flask.jsonify({"cache": str(flask.current_app.config["cache"].get_all())})


@bp.route("/write/<key>/<value>", methods=["GET"])
def write_string_to_cache(key, value):
    flask.current_app.config["cache"].write(key, value)
    return flask.redirect(flask.url_for("views_bp.get_all"))
