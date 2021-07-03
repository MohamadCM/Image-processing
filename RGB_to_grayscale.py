from PIL import Image
import numpy as np


def calculate_grayscale(image):
    opened_image = Image.open(image)
    image_vector = np.asarray(opened_image)
    grayscale_array = np.dot(image_vector[..., :3], [0.2989, 0.5870, 0.1140])
    for i in range(grayscale_array.shape[0]):
        for j in range(grayscale_array.shape[1]):
            grayscale_array[i, j] = int(grayscale_array[i, j])
    return grayscale_array


def main():
    print("Calculating grayscale image...")
    image = input("Please enter images name: ")
    grayscale = calculate_grayscale(image)
    img = Image.fromarray(np.uint8(grayscale * 255), 'L')
    img.save(image + "_grayscale" + ".png")
    img.show()
    print("Done!")


if __name__ == "__main__":
    main()
