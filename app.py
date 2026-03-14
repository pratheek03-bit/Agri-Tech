import os
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, render_template, send_from_directory, url_for
from keras.models import load_model
from services.locations import LocationService
from services.weather_service import get_weather

# ==========================
# App Initialization
# ==========================
app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed image types
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

# Path to trained model
MODEL_PATH = "model/disease_model.h5"
model = load_model(MODEL_PATH, compile=False)

# Disease classes
classes = [
    "Healthy",
    "Leaf Spot",
    "Early Blight",
    "Late Blight"
]

# Initialize location service
location_service = LocationService()

# ==========================
# Helper Functions
# ==========================
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


# ==========================
# Routes
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan")
def scan():
    return render_template("scan.html")


@app.route("/result")
def result():
    return render_template("result.html")
  # Save uploaded image
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Preprocess and predict
    processed_image = preprocess_image(filepath)
    prediction = model.predict(processed_image)
    class_index = int(np.argmax(prediction))
    confidence = float(np.max(prediction))
    disease = classes[class_index]

    # Optional: Location & weather
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    location_data, weather_data = None, None

    if latitude and longitude:
            location_data = location_service.get_location_from_coordinates(latitude, longitude)
            weather_data = get_weather(latitude, longitude)

        # Prepare final result
    result = {
        "prediction": {
            "disease": disease,
            "confidence": round(confidence * 100, 2)
        },
        "location": location_data,"weather": weather_data,"image_url": url_for("uploaded_file",filename=file.filename)
            }

    return jsonify(result)
    
    return jsonify({"error":str(e)}), 500


# ==========================
# Serve Uploaded Images
# ==========================
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ==========================
# Run Application
# ==========================
if __name__ == "__main__":
    app.run(debug=True, port=5000)