import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Cette fonction tronc la list en partant de l'index start
    jusqu'a l'index end si il est valide.
    """
    if not isinstance(family, list):
        raise ValueError(
            "Le paramètre family doit être une liste."
            )
    if any(not isinstance(sublist, list) for sublist in family):
        raise ValueError(
            "Tous les éléments de family doivent être des listes."
            )
    if len(family) == 0:
        raise ValueError("Family est vide.")
    max_len = len(family[0])
    for sublist in family:
        if len(sublist) != max_len:
            raise ValueError(
                "Toutes les sous-listes dans family doivent \
                    avoir la même taille.")
    # Convertir la liste en tableau NumPy
    family_np = np.array(family)
    if len(set(map(len, family_np))) != 1:
        raise ValueError("Toutes les sous-listes dans \
                        family doivent avoir la même taille.")
    # Afficher la forme du tableau original
    print(f"My shape is: {family_np.shape}")
    # Obtenir la sous-liste en utilisant le slicing (positif début négatif fin)
    new_family_np = family_np[start:end]
    print(f"My shape is: {new_family_np.shape}")
    return new_family_np.tolist()
