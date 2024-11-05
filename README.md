# Fashion Item Classifier with CNN

This project is a **Fashion Item Classifier** built using Convolutional Neural Networks (CNN) and deployed with **Streamlit**. The classifier is trained on the Fashion MNIST dataset to recognize different categories of clothing items. Users can upload an image of a clothing item, and the model will predict its category.

## Table of Contents
- [Demo](#demo)
- [Project Overview](#project-overview)
- [Model Details](#model-details)
- [How to Use](#how-to-use)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Future Improvements](#future-improvements)

---

## Demo
[LINK](https://fashion-item-classifier-with-cnn.streamlit.app/)

## Project Overview
The Fashion Item Classifier identifies the category of a clothing item uploaded by a user. It is based on the Fashion MNIST dataset, which contains images in 10 categories: 
- T-shirt/top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle boot

The app provides a user-friendly interface where users can upload an image and receive a prediction of the item category.

## Model Details
The CNN model is trained on the Fashion MNIST dataset. It uses multiple convolutional and pooling layers to extract features, followed by dense layers to classify the image into one of 10 categories.

- **Dataset**: Fashion MNIST
- **Model Architecture**: CNN (Convolutional Neural Network)
- **Framework**: TensorFlow/Keras

## How to Use
+ Run the Streamlit app.
+ Upload an image of a clothing item (preferably grayscale and similar to Fashion MNIST style).
+ View the model's prediction of the item category.

## File Structure
+ app.py: The main application file that loads the model and runs the Streamlit app.
+ model.keras: Pre-trained CNN model file.
+ requirements.txt: Contains the list of dependencies required to run the app.

## Dependencies
+ streamlit==1.25.0
+ tensorflow==2.13.0
+ Pillow==9.2.0
+ numpy==1.23.0

These packages are listed in requirements.txt and can be installed with:

## Future Improvements
+ Expand Model: Explore larger or more complex models for improved accuracy.
+ Additional Dataset: Train the model on additional fashion datasets for greater versatility.
+ Deployment: Deploy the app to a cloud platform (e.g., Heroku, AWS) for public access.
