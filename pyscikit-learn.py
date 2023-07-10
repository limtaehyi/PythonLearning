# !! -- pip install -U scikit-learn numpy matplotlib -- !!

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_iris, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# 예제 1: 회귀 분석
def linear_regression_example():
    print("Example 1: Linear Regression")
    
    x_train = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y_train = np.array([2, 4, 6, 8, 10])

    model = LinearRegression()
    model.fit(x_train, y_train)

    x_test = np.array([6, 7, 8, 9, 10]).reshape(-1, 1)
    y_test = np.array([12, 14, 16, 18, 20])

    y_pred = model.predict(x_test)

    print("Predictions:", y_pred)

    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)
    print("")

# 예제 2: 분류
def classification_example():
    print("Example 2: Classification")

    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("")

# 예제 3: 클러스터링
def clustering_example():
    print("Example 3: Clustering")

    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

    kmeans = KMeans(n_clusters=4)
    pred_y = kmeans.fit_predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=pred_y)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red')
    plt.show()
    print("")

# 모든 예제 실행
linear_regression_example()
classification_example()
clustering_example()
