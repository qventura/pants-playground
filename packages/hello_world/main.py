from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():    
    print("SUCCESS")

    return "Success"

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
