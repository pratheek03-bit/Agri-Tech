import tensorflow as tf
import numpy as np
import os
from keras.preprocessing import image
from keras.models import load_model

# Load trained model
model = load_model("models/crop_model.h5")

# Dataset folder
dataset_path = "dataset/color"

# Get class names
class_names = sorted(os.listdir(dataset_path))

# Test image
img_path = "test_images/leaf.jpg"

# Load image
img = image.load_img(img_path, target_size=(224,224))

# Convert image to array
img_array = image.img_to_array(img)

# Expand dimension
img_array = np.expand_dims(img_array, axis=0)

# Normalize
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)

# Get predicted class
predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction) * 100

# Split crop and disease
crop, disease = predicted_class.split("___")

print("\nPrediction Result")
print("--------------------")
print("Crop:", crop)
print("Disease:", disease)
print("Confidence:", round(confidence,2), "%")