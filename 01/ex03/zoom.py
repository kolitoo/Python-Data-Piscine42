from load_image import ft_load
import numpy as np

def main():
    """
    
    """
    pixels = ft_load("animal.jpeg")
    sliced_pixels = pixels[0:400, 0:400]
    print("Shape after slicing:", sliced_pixels.shape)
    print(sliced_pixels)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
