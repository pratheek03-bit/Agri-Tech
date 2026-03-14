import tensorflow as tf
import numpy as np
import os
from keras.preprocessing import image

class PredictionService:

    def __init__(self):
        # Load trained model
        self.model = tf.keras.models.load_model("models/crop_model.h5")

        # Dataset folder for class names
        dataset_path = "dataset/color"

        # Get class names
        self.class_names = sorted(os.listdir(dataset_path))


    def predict_disease(self, img_path):

        try:
            # Load image
            img = image.load_img(img_path, target_size=(224, 224))

            # Convert image to array
            img_array = image.img_to_array(img)

            # Expand dimensions
            img_array = np.expand_dims(img_array, axis=0)

            # Normalize
            img_array = img_array / 255.0

            # Predict
            prediction = self.model.predict(img_array)

            # Get predicted class
            index = np.argmax(prediction)
            predicted_class = self.class_names[index]

            confidence = float(np.max(prediction) * 100)

            # Split crop and disease
            crop, disease = predicted_class.split("___")

            return {
                "crop": crop,
                "disease": disease,
                "confidence": round(confidence, 2)
            }

        except Exception as e:

            return {
                "error": str(e)
            }