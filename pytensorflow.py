import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models, utils

# 예제 1: 선형 회귀
def linear_regression_example():
    print("Example 1: Linear Regression")
    
    x_train = np.array([1, 2, 3, 4, 5], dtype=float)
    y_train = 2 * x_train + 1

    model = keras.Sequential([
        keras.layers.Dense(units=1, input_shape=[1])
    ])

    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=500)

    x_test = np.array([6, 7, 8, 9, 10], dtype=float)
    y_test = model.predict(x_test)

    print("Predictions:", y_test[:, 0])
    print("")

# 예제 2: 이미지 분류 - CNN
def image_classification_example():
    print("Example 2: Image Classification with CNN")

    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
    train_images, test_images = train_images / 255.0, test_images / 255.0

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=10, batch_size=64)

    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print("Test accuracy:", test_acc)
    print("")

# 예제 3: 시계열 예측 - RNN (LSTM)
def time_series_prediction_example():
    print("Example 3: Time Series Prediction with RNN (LSTM)")

    sequence_length = 10
    x_train = np.random.rand(1000, sequence_length, 1)
    y_train = np.sum(x_train, axis=1)

    model = keras.Sequential([
        layers.LSTM(50, input_shape=(sequence_length, 1), return_sequences=True),
        layers.LSTM(30),
        layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=100, batch_size=64)

    x_test = np.random.rand(100, sequence_length, 1)
    y_test = np.sum(x_test, axis=1)
    y_pred = model.predict(x_test)

    print("Predictions:", y_pred[:, 0])
    print("")

# 모든 예제 실행
linear_regression_example()
image_classification_example()
time_series_prediction_example()
