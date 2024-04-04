from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys


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
        check_img = ft_load(path)
        if not check_img.size:
            raise AssertionError("Loading problem.")
        image = Image.open(path)
        sliced_image = image.crop((400, 100, 800, 500))
        # sliced_image.show()
        sliced_image_gray = sliced_image.convert('L')
        # sliced_image_gray.show()
        sliced_pixels = np.array(sliced_image_gray)
        print(f"New shape after cropping: {sliced_pixels.shape}")
        # print l'ajout nouvelle dimension le long de l'axe des colonnes
        print(np.expand_dims(sliced_pixels, axis=2))
        plt.imshow(sliced_pixels, cmap='gray')
        plt.axis('on')
        plt.show()
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")


if __name__ == "__main__":
    main()
