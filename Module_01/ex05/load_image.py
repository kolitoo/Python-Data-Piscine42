from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    This fonction check if there is no errors.
    It print the format and the shame of the pixels of the image.
    The display change if the number channel is 1 or more.
    It return the image in np.npdarray form.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        # Charger l'image
        img = Image.open(path)
        # Vérifier le format de l'image
        if not path.lower().endswith(("jpg", "jpeg", "png")):
            raise AssertionError(
                "Only JPG, JPEG and PNG formats are supported."
            )

        # Imprimer le format de l'image
        print("Format:", img.format)

        # Obtenir les pixels de l'image
        pixels = np.array(img)

        # Afficher les pixels de l'image en format RGB
        print(f"The shape of image is: {pixels.shape}")
        if len(pixels.shape) != 2:
            print(pixels)
        else:
            print(np.expand_dims(pixels, axis=2))

        return pixels

    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return np.array([])
