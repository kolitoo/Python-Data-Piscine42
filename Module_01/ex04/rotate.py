from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
import os


def transpose_image(image):
    """
    """
    width, height = image.size
    transpose_image = Image.new(image.mode, (height, width))
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            transpose_image.putpixel((y, x), pixel)
    return transpose_image


def main():
    """
    This main check if everything is ok for the image (with ft_load).
    It zoom the image with crop and print it.
    It convert the image in grey. and print the new shape.
    Plt is use to print the scale on the image
    """
    try:
        if len(sys.argv) == 2:
            path = sys.argv[1]
        else:
            path = "animal.jpeg"
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        if not path.lower().endswith(("jpg", "jpeg", "png")):
            raise AssertionError(
                "Only JPG, JPEG and PNG formats are supported."
                )

        image = Image.open(path)
        sliced_image = image.crop((400, 100, 800, 500))
        sliced_image_gray = sliced_image.convert('L')
        sliced_image_gray.save(f"crop_{path}.jpg")
        ft_load(f"crop_{path}.jpg")

        transpose_img = transpose_image(sliced_image_gray)
        print(f"New shape after Transpose: {np.array(transpose_img).shape}")
        print(np.array(transpose_img))

        plt.imshow(transpose_img, cmap='gray')
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")


if __name__ == "__main__":
    main()
