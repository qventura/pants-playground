import os 
from flask import Flask

print("OK1")

app = Flask(__name__)

@app.route("/")
def main():    
    print("SUCCESSSSSS")

    return "Success"

print("__name__", __name__)

if __name__ == "hello_world.main":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
