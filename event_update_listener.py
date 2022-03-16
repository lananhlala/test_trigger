# app.py
from flask import Flask, request

app = Flask(__name__)

@app.post("/trigger")
def update_issue():
    data = request.get_json()
    print(data)
    return "Received", 201
