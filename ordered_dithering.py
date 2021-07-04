import numpy as np
import matplotlib.pyplot as plt

from RGB_to_grayscale import calculate_grayscale
from utils import print_line


def calculate_ordered_dithering(image_vector, threshold_map):
    result = np.empty(image_vector.shape)
    map_rows, map_columns = threshold_map.shape[0], threshold_map.shape[1]
    image_rows, image_columns = image_vector.shape[0], image_vector.shape[1]
    # Moving the threshold over the image's vector
    for i in range(0, image_rows, map_rows):
        for j in range(0, image_columns, map_columns):
            for k in range(map_rows):
                for p in range(map_columns):
                    if image_vector[i + k, j + p] < threshold_map[k, p]:
                        result[i + k, j + p] = 0
                    else:
                        result[i + k, j + p] = 255
    return result


def create_threshold_map(n):
    # Converting n to closest power of 2
    count = 0
    if n and not (n & (n - 1)):
        power_of_two = n
    else:
        while n != 0:
            n >>= 1
            count += 1
        power_of_two = 1 << count
    # Calling recursive function
    return (recursive_map_finder(power_of_two)) / (power_of_two * power_of_two)


def recursive_map_finder(n):
    # Exiting condition
    if n == 2:
        return np.array([[0, 2], [3, 1]], "int")
    else:
        # Calling recursive functions
        next_level_map = recursive_map_finder(n >> 1)
        # Formula for threshold map
        return np.bmat(
            [
                [4 * next_level_map, 4 * next_level_map + 2],
                [4 * next_level_map + 3, 4 * next_level_map + 1],
            ]
        )


def main():
    input_image = input("Please enter image's name: ")
    n = input("Please enter map's size (n): ")
    print("Calculating")
    # print_line()
    threshold_map = 255 * create_threshold_map(int(n))
    # print("Grayscale threshold map:")
    # print(threshold_map)
    # print_line("-")
    # Calculating
    grayscale_array = calculate_grayscale(input_image)
    result = calculate_ordered_dithering(grayscale_array, threshold_map)
    # Showing results
    plt.axis('off')
    plt.title("Normal grayscale image")
    plt.imshow(grayscale_array, cmap='gray', vmin=0, vmax=255)
    plt.show()

    plt.axis('off')
    plt.title("Dithered image")
    plt.imshow(result, cmap='gray', vmin=0, vmax=255)
    plt.show()
    # Saving image
    plt.imsave(arr=result, fname=(input_image + "_dithered.png"), cmap='gray', vmin=0, vmax=255)

    print("DONE!")


if __name__ == "__main__":
    main()
