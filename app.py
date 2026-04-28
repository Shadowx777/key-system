from flask import Flask, request, jsonify
from pymongo import MongoClient
import time

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin@123@cluster0.b982h9o.mongodb.net/keydb")
db = client["keydb"]
keys = db["keys"]

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    key = data.get("key")
    device = data.get("device")

    k = keys.find_one({"key": key})

    if not k:
        return jsonify({"status": "invalid"})

    if k["status"] != "active":
        return jsonify({"status": "blocked"})

    if time.time() > k["expiry"]:
        return jsonify({"status": "expired"})

    if k["device"] is None:
        keys.update_one({"key": key}, {"$set": {"device": device}})
        return jsonify({"status": "ok"})

    if k["device"] != device:
        return jsonify({"status": "used_on_other_device"})

    return jsonify({"status": "ok"})

app.run(host="0.0.0.0", port=3000)
