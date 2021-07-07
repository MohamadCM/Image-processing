"""
    Author: Mohamad Chamanmotlagh
    Email: m.chamanmotlagh[at]gmail.com
    July 2021
"""
from PIL import Image


def calculate_captcha(image):
    opened_image = Image.open(image)
    return ""


def main():
    input_image = input("Please enter image's name: ")
    print("Calculating result...")
    captcha_text = calculate_captcha(input_image)
    print("Done!")
    print("The captcha text is: " + captcha_text)


if __name__ == "__main__":
    main()
