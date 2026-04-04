from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__)  # Flask will look for /templates automatically

IMAGE_FOLDER = "img"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/images")
def get_images():
    files = os.listdir(IMAGE_FOLDER)
    images = [
        f"/img/{f}" for f in files
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    return jsonify(images)

@app.route("/img/<filename>")
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)