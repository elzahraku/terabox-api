from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "Terabox Python API Running"})

@app.route("/api/terabox", methods=["GET"])
def terabox():
    url = request.args.get("url")

    if not url:
        return jsonify({"status": False, "error": "URL is required"}), 400

    try:
        api_url = f"https://terabox.com/api/shorturlinfo?shorturl={url}"
        response = requests.get(api_url)
        data = response.json()

        return jsonify({
            "status": True,
            "result": data
        })

    except Exception as e:
        return jsonify({
            "status": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
