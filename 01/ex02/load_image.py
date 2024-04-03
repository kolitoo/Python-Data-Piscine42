from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Fonction qui charge une image, verifie son format et print les pixels sous forme RGB.
    """
    try:
        # Charger l'image
        img = Image.open(path)

        # Vérifier le format de l'image
        img_format = img.format
        if img_format not in ['JPEG', 'JPG']:
            raise ValueError("Wrong format, need JPG or JPEG")
        
        # Imprimer le format de l'image
        print("Format:", img_format)
        
        # Obtenir les pixels de l'image
        pixels = np.array(img)
        
        # Afficher les pixels de l'image en format RGB
        print(f"The shape of image is: {pixels.shape}")
        print(pixels)
        
        return pixels
    
    except FileNotFoundError as e:
        print("File not found")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Une erreur s'est produite lors du chargement de l'image:", str(e))