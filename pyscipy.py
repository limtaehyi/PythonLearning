import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, linalg, interpolate, stats, fftpack


# Optimization
def optimization_example():
    def f(x):
        return x**2 + 5 * np.sin(x)

    minima = optimize.minimize(f, x0=1)
    print("Optimization: Minima:", minima.x)
    
    
# Linear Algebra
def linear_algebra_example():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5], [7]])

    x = linalg.solve(A, B)
    print("Linear Algebra: Solution:", x)


# Eigenvalue and eigenvector calculation
def eig_example():
    A = np.array([[1, 2], [3, 4]])
    eigvals, eigvecs = linalg.eig(A)

    print("Eigenvalues:", eigvals)
    print("Eigenvectors:", eigvecs)
    
    
# Interpolation
def interpolation_example():
    x = np.arange(5)
    y = np.sin(x)
    interp_f = interpolate.interp1d(x, y, kind='linear')
    x_new = np.linspace(0, 4, 100)
    y_new = interp_f(x_new)

    plt.plot(x, y, 'o', x_new, y_new, '-')
    plt.title("Interpolation")
    plt.show()
    
    
# Statistics
def stats_example():
    data = np.random.normal(size=100)
    desc = stats.describe(data)
    mean, var, skew, kurt = desc.mean, desc.variance, desc.skewness, desc.kurtosis

    print("Statistics: Mean:", mean)
    print("Variance:", var)
    print("Skewness:", skew)
    print("Kurtosis:", kurt)


# FFT (Fast Fourier Transform)
def fft_example():
    t = np.linspace(0, 1, 500)
    y = np.sin(50 * 2 * np.pi * t) + 0.5 * np.sin(80 * 2 * np.pi * t)
    y_fft = fftpack.fft(y)
    freqs = fftpack.fftfreq(len(y))

    plt.plot(np.abs(freqs), np.abs(y_fft))
    plt.title("FFT (Fast Fourier Transform)")
    plt.show()
    
    
# Run all examples
if __name__ == "__main__":
    optimization_example()
    linear_algebra_example()
    eig_example()
    interpolation_example()
    stats_example()
    fft_example()
