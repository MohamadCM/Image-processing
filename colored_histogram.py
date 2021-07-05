"""
    Author: Mohamad Chamanmotlagh
    Email: m.chamanmotlagh[at]gmail.com
    July 2021
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def calculate_colored_histogram(image):
    opened_image = Image.open(image)
    image_vector = np.asarray(opened_image)
    red_range, green_range, blue_range = [0] * 256, [0] * 256, [0] * 256
    rows, columns = image_vector.shape[0], image_vector.shape[1]
    for i in range(rows):
        for j in range(columns):
            value = image_vector[i, j]
            red_range[value[0]] = red_range[value[0]] + 1
            green_range[value[1]] = green_range[value[1]] + 1
            blue_range[value[2]] = blue_range[value[2]] + 1
    return [red_range, green_range, blue_range]


def main():
    input_image = input("Please enter images name: ")
    print("Calculating colored histogram...")
    histograms = calculate_colored_histogram(input_image)
    red_range, green_range, blue_range = histograms[0], histograms[1], histograms[2]
    plt.title("Colored histogram of " + input_image)
    x_axis = range(0, 256)
    plt.bar(x_axis, red_range, color='r')
    plt.bar(x_axis, green_range, color='g')
    plt.bar(x_axis, blue_range, color='b')
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.show()
    print("Done!")


if __name__ == "__main__":
    main()
