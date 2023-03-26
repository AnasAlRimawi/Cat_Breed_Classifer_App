import cv2
from tensorflow import keras
import tensorflow as tf
import numpy as np

model = keras.models.load_model('meow')
model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['acc'])
classes = np.array(['Abyssinian', 'Bengal', 'Birman', 'Bombay', 'British', 'Egyptian', 'Maine', 'Persian', 'Ragdoll', 'Russian', 'Siamese', 'Sphynx'])

# Process image (input) for the model
def process(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224,224))
    img = tf.keras.applications.mobilenet.preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img

def get_prediction(img):
    pred = process(img)
    return classes[np.argmax(model.predict(pred, verbose = 0), axis=1)]

