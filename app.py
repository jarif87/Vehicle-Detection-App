from flask import Flask, request, render_template, url_for
import cv2
import numpy as np
from PIL import Image
import string
import random
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['INITIAL_FILE_UPLOADS'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'webp'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Cascade classifiers
CAR_CASCADE_SRC = 'static/cascade/cars.xml'
BUS_CASCADE_SRC = 'static/cascade/Bus_front.xml'

# Utility functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_unique_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10)) + '.png'

def process_image(image):
    # Convert to RGB and resize
    image = image.convert('RGB')  # Ensure RGB format
    image = image.resize((450, 250))
    image_arr = np.array(image)
    grey = cv2.cvtColor(image_arr, cv2.COLOR_RGB2GRAY)  # Use RGB2GRAY for PIL images

    # Load cascades
    car_cascade = cv2.CascadeClassifier(CAR_CASCADE_SRC)
    bus_cascade = cv2.CascadeClassifier(BUS_CASCADE_SRC)
    
    # Check if cascades loaded successfully
    if car_cascade.empty() or bus_cascade.empty():
        raise ValueError("Failed to load cascade classifiers")

    # Detect buses
    bcnt = 0
    bus = bus_cascade.detectMultiScale(grey, 1.1, 1)
    for (x, y, w, h) in bus:
        cv2.rectangle(image_arr, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green for buses
        bcnt += 1

    # Detect cars
    ccnt = 0
    cars = car_cascade.detectMultiScale(grey, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(image_arr, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Red for cars
        ccnt += 1

    return image_arr, ccnt, bcnt

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", full_filename='images/white_bg.jpg', pred=None, error=None)

    if request.method == "POST":
        # Check if file is uploaded
        if 'image_upload' not in request.files:
            return render_template("index.html", full_filename='images/white_bg.jpg', error="No file uploaded", pred=None)

        image_upload = request.files['image_upload']
        if image_upload.filename == '':
            return render_template("index.html", full_filename='images/white_bg.jpg', error="No file selected", pred=None)

        if not allowed_file(image_upload.filename):
            return render_template("index.html", full_filename='images/white_bg.jpg', error="Invalid file type", pred=None)

        # Process image
        try:
            image = Image.open(image_upload)
            image_arr, ccnt, bcnt = process_image(image)

            # Save processed image
            name = generate_unique_name()
            full_filename = f'uploads/{name}'
            img = Image.fromarray(image_arr, 'RGB')
            img.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))

            # Result message
            result = f"{ccnt} cars and {bcnt} buses found"
            return render_template('index.html', full_filename=full_filename, pred=result, error=None)
        except Exception as e:
            return render_template("index.html", full_filename='images/white_bg.jpg', error=f"Error processing image: {str(e)}", pred=None)

if __name__ == '__main__':
    os.makedirs(app.config['INITIAL_FILE_UPLOADS'], exist_ok=True)
    app.run(debug=True)