from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def calculate_histogram(image):
    grayscale_image = Image.open(image).convert('LA')
    grayscale_array = np.asarray(grayscale_image)
    x_range = [0] * 256
    for i in range(grayscale_array.shape[0]):
        for j in range(grayscale_array.shape[1]):
            value = grayscale_array[i, j, 0]
            x_range[value] = x_range[value] + 1
    return x_range


def main():
    print("Calculating grayscale histogram...")
    img = input("Please enter images name: ")
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
