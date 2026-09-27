from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Backend Tier Running"


@app.route("/api")
def api():
    return {
        "application": "Three Tier DevOps Application",
        "status": "success",
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
