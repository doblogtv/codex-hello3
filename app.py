from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "これは / のトップページです（codex-hello3）"

@app.route("/hello")
def hello():
    return "Hello Codex 3!"

@app.route("/image")
def image():
    return """
    <!doctype html>
    <html lang=\"ja\">
    <head>
        <meta charset=\"utf-8\">
        <title>Codex 3 Image</title>
    </head>
    <body>
        <h1>Codex 3 ロゴ</h1>
        <img src=\"/static/logo.svg\" alt=\"Codex 3 logo\" width=\"200\" height=\"200\">
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
