import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
import os

# ===============================
# Dataset Path
# ===============================

dataset_path = r"C:\Users\darshangowda\.cache\kagglehub\datasets\vipoooool\new-plant-diseases-dataset\versions\2"

train_dir = os.path.join(dataset_path, "New Plant Diseases Dataset(Augmented)", "train")
valid_dir = os.path.join(dataset_path, "New Plant Diseases Dataset(Augmented)", "valid")

print("Training Folder:", train_dir)
print("Validation Folder:", valid_dir)

# ===============================
# Image Preprocessing
# ===============================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=25,
    zoom_range=0.2,
    horizontal_flip=True
)

valid_datagen = ImageDataGenerator(
    rescale=1./255
)

# ===============================
# Load Dataset
# ===============================

train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical"
)

valid_data = valid_datagen.flow_from_directory(
    valid_dir,
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical"
)

print("Total Classes:", train_data.num_classes)

# ===============================
# CNN Model
# ===============================

model = Sequential()

model.add(Conv2D(32,(3,3),activation="relu",input_shape=(224,224,3)))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64,(3,3),activation="relu"))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(128,(3,3),activation="relu"))
model.add(MaxPooling2D(2,2))

model.add(Flatten())

model.add(Dense(512,activation="relu"))
model.add(Dropout(0.5))

model.add(Dense(train_data.num_classes,activation="softmax"))

# ===============================
# Compile Model
# ===============================

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ===============================
# Train Model
# ===============================

history = model.fit(
    train_data,
    validation_data=valid_data,
    epochs=10
)

# ===============================
# Save Model
# ===============================

model.save("crop_model.h5")

print("Model training completed successfully!")