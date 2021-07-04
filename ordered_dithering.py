import numpy
import numpy as np


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
    # input_image = input("Please enter image's name: ")
    n = input("Please enter map's size (n): ")
    threshold_map = create_threshold_map(int(n))
    print(threshold_map)


if __name__ == "__main__":
    main()
