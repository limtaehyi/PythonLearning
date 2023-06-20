import numpy as np
import matplotlib.pyplot as plt

# 기본 막대그래프 그리기
def plot_bar_graph():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([10, 15, 20, 25, 30])

    plt.bar(x, y)
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")
    plt.title("Bar Graph")
    plt.show()

# 라인 그래프 그리기
def plot_line_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")
    plt.title("Line Graph")
    plt.show()

# 산포도 그리기
def plot_scatter_plot():
    x = np.random.randn(50)
    y = np.random.randn(50)

    plt.scatter(x, y)
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")
    plt.title("Scatter Plot")
    plt.show()

# 히스토그램 그리기
def plot_histogram():
    data = np.random.randn(1000)

    plt.hist(data, bins=20)
    plt.xlabel("X Axis Label")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

# 서브플롯을 사용하여 여러 그래프를 하나의 Figure에 그리기
def plot_subplot():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    fig, axes = plt.subplots(2, 1)

    axes[0].plot(x, y1)
    axes[0].set_title("Sine")

    axes[1].plot(x, y2)
    axes[1].set_title("Cosine")

    fig.tight_layout()
    plt.show()

# 색상 및 스타일 사용자 정의
def plot_custom_styles_colors():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label="Sine", color="red", linestyle="--")
    plt.plot(x, y2, label="Cosine", color="blue", linestyle="-.")

    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")
    plt.title("Customized Line Styles & Colors")
    plt.legend(loc="best")
    plt.show()

# 그래프 함수 실행
plot_bar_graph()
plot_line_graph()
plot_scatter_plot()
plot_histogram()
plot_subplot()
plot_custom_styles_colors()
