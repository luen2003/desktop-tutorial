import cv2
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical
import tkinter as tk
from tkinter import filedialog, messagebox

# Load and preprocess the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255
train_images = np.expand_dims(train_images, axis=-1)
test_images = np.expand_dims(test_images, axis=-1)
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the model
model = Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')  # 10 output units for digits 0-9
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

def load_and_predict_image(file_path):
    # Load and preprocess the image
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))
    image = cv2.bitwise_not(image)  # Invert the colors for better prediction
    image = image.astype('float32') / 255
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=-1)

    # Predict the digit
    prediction = np.argmax(model.predict(image))
    return prediction

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        prediction = load_and_predict_image(file_path)
        messagebox.showinfo("Prediction Result", f"Predicted Digit: {prediction}")

# Create the main GUI window
root = tk.Tk()
root.title("Digit Prediction")
root.geometry("300x150")

# Create a button to select an image file
select_button = tk.Button(root, text="Select Digit Image", command=select_file)
select_button.pack(expand=True)

# Start the GUI event loop
root.mainloop()
