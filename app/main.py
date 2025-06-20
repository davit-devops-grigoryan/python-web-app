from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    a = os.getenv("VERSION_A", "0")
    b = os.getenv("VERSION_B", "0")
    c = os.getenv("VERSION_C", "0")
    commit_sha = os.getenv("COMMIT_SHA", "0")
    return f'Hello, version "{a}_{b}_{c}_{commit_sha}"'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

