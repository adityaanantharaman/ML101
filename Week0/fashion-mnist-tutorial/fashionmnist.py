# -*- coding: utf-8 -*-
"""FashionMNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-QFyh8QWe-OalONnORmo3sFSRTQoe535

# First import dependencies
We require:


1.   tensorflow  (Google's ML framework)
2.   keras           (high level api working on top of tensoflow)
3.   numpy         (for fast numerical computation)
4.   matplotlib   (for ploting images)
"""

import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

"""# Download dataset : Fashion MNIST dataset
## Dataset that consists of 70,000 images of 10 different categories of clothing
## Each image of size 28 by 28 (black and white)
## Dataset is split into train/test images with a 6:1 ratio
"""

fashion_mnist=keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()

print('train images shape : '+str(train_images.shape))
print('train labels shape : '+str(train_labels.shape))

print('test images shape : '+str(test_images.shape))
print('test labels shape : '+str(test_labels.shape))

"""## Currently the pixel values in these images range from 0-255. We normalize these values and bring it down to the range 0-1"""

train_images=train_images/255
test_images=test_images/255

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

"""## Pick a random image from the train data and plot it along with the class it belongs to"""

n=np.random.randint(0,60000)
img=train_images[n,:,:]
plt.imshow(img)
print('category is : '+class_names[train_labels[n]])

"""## Creating a model in keras to train the dataset on"""

model=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation=tf.nn.relu),
    keras.layers.Dense(10,activation=tf.nn.softmax)
])

"""# Compiling the model we just created by giving in 3 parameters : 


## *   Optimizer (how we reduce the loss function)
## *   Loss (the measure with which we calculate distance between the actual and predicted values)
## * Metrics (what we want our model to improve on)
"""

model.compile(optimizer=tf.train.AdamOptimizer(),
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

"""# The actual training process
## We give the train images and train labels as inputs to train the model
"""

model.fit(train_images,train_labels,epochs=10)

"""# Evaluating our model on previously unseen test data"""

model.evaluate(test_images,test_labels)

"""# Selecting a random image from the test dataset and predicting the class that it belongs to"""

n=np.random.randint(0,10000)
test_img=test_images[n,:,:].reshape(1,28,28)
predicted_class_number=np.argmax(model.predict(test_img))
predicted_class=class_names[predicted_class_number]
plt.imshow(test_img[0,:,:])
print('predicted class is : '+predicted_class)

