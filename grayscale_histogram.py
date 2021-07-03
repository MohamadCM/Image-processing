from PIL import Image
from RGB_to_grayscale import calculate_grayscale
import numpy as np
import matplotlib.pyplot as plt


def calculate_histogram(image):
    grayscale_array = calculate_grayscale(image)
    x_range = [0] * 256
    for i in range(grayscale_array.shape[0]):
        for j in range(grayscale_array.shape[1]):
            value = grayscale_array[i, j]
            x_range[value] = x_range[value] + 1
    return x_range


def main():
    img = input("Please enter images name: ")
    print("Calculating grayscale histogram...")
    histogram = calculate_histogram(img)
    plt.plot(np.array(histogram), "-k")
    plt.title("Grayscale histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Count")
    plt.grid(linestyle='--', linewidth=0.5)
    plt.show()
    print("Done!")


if __name__ == "__main__":
    main()
