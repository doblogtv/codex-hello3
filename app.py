from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "これは / のトップページです（codex-hello3）"

@app.route("/hello")
def hello():
    return "Hello Codex 3!"

if __name__ == "__main__":
    app.run(debug=True)
