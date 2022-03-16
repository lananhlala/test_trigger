# app.py
from flask import Flask, request

app = Flask(__name__)

@app.post("/trigger")
def update_issue():
    data = request.get_json()
    print(data)
    return "Received", 201

if __name__ == "__main__":
    # co ve dang loi khi request den url nay
    app.run(port=443, debug=True)