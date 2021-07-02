from PIL import Image


def main():
    print("Calculating grayscale image...")
    from PIL import Image
    img = Image.open('image.jpg').convert('LA')  # Converting image to grayscale
    print("Done!")


if __name__ == "__main__":
    main()
