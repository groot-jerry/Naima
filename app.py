from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

IMAGE_FOLDER = "img"

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/gallery")
def gallery():
    return send_from_directory(".", "gallery.html")

@app.route("/img")
def get_images():
    files = os.listdir(IMAGE_FOLDER)
    images = [f"/img/{f}" for f in files]  # include all files
    return jsonify(images)

@app.route("/img/<filename>")
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)