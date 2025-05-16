# Vehicle Detection & Classification App

A Flask-based web application that detects and counts cars and buses in uploaded images using OpenCV Haar cascades. The app features a modern, responsive UI with image previews, animated cards, and a vibrant design powered by Materialize CSS.

## Features
- Upload images (PNG, JPG, JPEG, WebP) to detect vehicles.
- Detects both cars (red rectangles) and buses (green rectangles) together.
- Displays processed images with vehicle counts (e.g., "3 cars and 2 buses found").
- Attractive UI with gradient backgrounds, hover animations, and a loading spinner.
- Responsive design for mobile, tablet, and desktop.
- Error handling for invalid files or processing issues.
- Image preview before processing.

## Prerequisites
- Python 3.8+
- pip for installing dependencies
- Git (optional, for cloning)

## Installation

1. **Clone the Repository** (or download the project files):
   ```bash
   git clone <repository-url>
   cd vehicle-detection-app

2. **Create a Virtual Environment (recommended):**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
#### Ensure requirements.txt is in the project root:


```pip install -r requirements.txt```


4. **Contents of requirements.txt:**
```
flask
opencv-python
numpy
pillow
werkzeug
```

5. **Set Up Directories:**
### Create the uploads directory:
```
mkdir -p static/uploads
```

6. **Ensure the following files are in place:**
```
static/cascade/cars.xml

static/cascade/Bus_front.xml

static/images/white_bg.jpg
```
7. **Project Structure**
```
vehicle-detection-app/
├── static/
│   ├── cascade/
│   │   ├── cars.xml           # Haar cascade for cars
│   │   ├── Bus_front.xml      # Haar cascade for buses
│   ├── uploads/               # Processed images
│   ├── images/
│   │   ├── white_bg.jpg       # Default image
│   ├── style.css              # Custom styles
├── templates/
│   ├── index.html             # Main HTML template
├── app.py                     # Flask application
├── requirements.txt           # Dependencies
├── README.md                  # This file
```

# Usage
1. Run the Application:

```
python app.py
The app will start in debug mode at http://127.0.0.1:5000.


```
# **Access the App:**
```
Open a browser and navigate to http://127.0.0.1:5000.
```

# **Upload an Image:**
- Click "Browse" to select an image (PNG, JPG, JPEG, or WebP).

- View the image preview.

- Click "Process" to detect vehicles.

- The result card will show the processed image with red (cars) and green (buses) rectangles, plus a count (e.g., "2 cars and 1 buses found").



