from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    print("Calculating grayscale image...")
    img = Image.open('image.jpg').convert('LA')  # Converting image to grayscale
    grayscale_array = np.asarray(img)
    x_range = []
    for i in range(256):
        x_range.append(0)
    print(grayscale_array.shape)
    for i in range(grayscale_array.shape[0]):
        for j in range(grayscale_array.shape[0]):
            value = grayscale_array[i, j, 0]
            x_range[value] = x_range[value] + 1
    plt.plot(np.array(x_range), "-k")
    plt.title("Grayscale histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Count")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()
    print("Done!")


if __name__ == "__main__":
    main()
