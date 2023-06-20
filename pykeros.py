import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist

def simple_sequential_model():
    X = np.random.random((100, 2))
    y = (X[:, 0] + X[:, 1]) > 1

    model = Sequential()
    model.add(Dense(16, input_dim=2, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=10, batch_size=32)

def multiclass_classification_model():
    X = np.random.random((100, 20))
    y = np.random.randint(0, 10, size=(100, 1))
    y = to_categorical(y)

    model = Sequential()
    model.add(Dense(64, input_dim=20, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=10, batch_size=32)

def cnn_image_classification_model():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape((-1, 28, 28, 1)).astype('float32') / 255.0
    X_test = X_test.reshape((-1, 28, 28, 1)).astype('float32') / 255.0
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

if __name__ == "__main__":
    print("\n--- Simple Sequential Model ---\n")
    simple_sequential_model()
    print("\n--- Multiclass Classification Model ---\n")
    multiclass_classification_model()
    print("\n--- CNN Image Classification Model ---\n")
    cnn_image_classification_model()
