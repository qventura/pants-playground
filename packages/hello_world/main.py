import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Success"


if __name__ == "hello_world.main":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
