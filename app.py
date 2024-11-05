import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load your saved model
model = tf.keras.models.load_model('model.keras')

# Define class names for the predictions
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Preprocess the uploaded image
def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28
    image = np.array(image) / 255.0  # Normalize to [0, 1]
    image = image.reshape(1, 28, 28, 1)  # Add batch and channel dimensions
    return image

# Streamlit app title and description
st.title("Fashion Item Classifier")
st.write("Upload a fashion item image, and the model will predict its category.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Classifying...")

    # Preprocess and make prediction
    image = preprocess_image(image)
    predictions = model.predict(image)
    predicted_class = class_names[np.argmax(predictions)]

    # Display the prediction
    st.write(f"Prediction: **{predicted_class}**")
