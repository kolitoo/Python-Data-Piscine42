import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """Inverts the color of the image reveived.
255 - the color of each pixel (R, G abd B)."""
    inverted_image = 255 - array
    return inverted_image


def ft_red(array):
    """
    Keep the red color of the RGB."""
    red_chan = array[:, :, 0]
    red_image = np.zeros_like(array, dtype=np.uint8)
    red_image[:, :, 0] = red_chan
    return red_image


def ft_green(array):
    """
    Keep the greed color of the RGB."""
    green_chan = array[:, :, 1]
    green_image = np.zeros_like(array, dtype=np.uint8)
    green_image[:, :, 1] = green_chan
    return green_image


def ft_blue(array):
    """
    Keep the blue color of the RGB."""
    blue_chan = array[:, :, 2]
    blue_image = np.zeros_like(array, dtype=np.uint8)
    blue_image[:, :, 2] = blue_chan
    return blue_image


def ft_grey(array):
    """
    Averaged the three colours of the RGB to put in grey."""
    sum_chan = np.sum(array, axis=2, dtype=np.uint32)
    grey_chan = sum_chan / 3
    grey_image = np.zeros_like(array, dtype=np.uint8)
    grey_image[:, :, 0] = grey_chan
    grey_image[:, :, 1] = grey_chan
    grey_image[:, :, 2] = grey_chan
    return grey_image


def print_nd_image(array):
    """
    Print Images."""
    plt.imshow(array)
    plt.axis('off')
    plt.show()
