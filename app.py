from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello")
def hello() -> str:
    """Return the current date and time as JSON."""
    now = datetime.now()
    return jsonify(date=now.strftime("%Y-%m-%d"), time=now.strftime("%H:%M:%S"))


def create_app() -> Flask:
    """Application factory used by WSGI servers."""
    return app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
