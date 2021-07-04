import numpy
import numpy as np


def create_threshold_map(n):
    return (recursive_map_finder(n)) / (n * n)


def recursive_map_finder(n):
    if n == 2:
        return np.array([[0, 2], [3, 1]], "int")
    else:
        next_level_map = recursive_map_finder(n >> 1)
        return np.bmat(
            [
                [4 * next_level_map, 4 * next_level_map + 2],
                [4 * next_level_map + 3, 4 * next_level_map + 1],
            ]
        )


def main():
    # input_image = input("Please enter image's name: ")
    n = input("Please enter map's size (n): ")
    threshold_map = create_threshold_map(int(n))
    print(threshold_map)


if __name__ == "__main__":
    main()
