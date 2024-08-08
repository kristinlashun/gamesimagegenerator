from flask import Flask, render_template, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

# Path to the folder containing game images
IMAGE_FOLDER = 'images'
TEXT_FILE = 'image_path.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['GET'])
def generate_image():
    images = os.listdir(IMAGE_FOLDER)
    if not images:
        return jsonify({"error": "No images available"}), 404
    image = random.choice(images)
    image_path = os.path.join(IMAGE_FOLDER, image)

    with open(TEXT_FILE, 'w') as f:
        f.write(image_path)

    return jsonify({"image_path": f"/images/{image}"})

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
