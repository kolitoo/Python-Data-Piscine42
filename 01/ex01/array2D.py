import numpy as np

# def slice_me(family: list, start: int, end: int) -> list:
#     for element in family:
#         element_len = len(element)
#     print(f"My shape is: ({len(family)}, {element_len})")
#     new_family = family[start:end]
#     for new_element in new_family:
#         new_element_len = len(new_element)
#     print(f"My shape is: ({len(new_family)}, {new_element_len})")
#     return family[start:end]

def slice_me(family: list, start: int, end: int) -> list:
    """
    Cette fonction tronc la list en partant de l'index start jusqu'a l'index end si il est valide
    """
    if not isinstance(family, list):
        raise ValueError("Le paramètre family doit être une liste.")
    if any(not isinstance(sublist, list) for sublist in family):
        raise ValueError("Tous les éléments de family doivent être des listes.")
    if len(family) == 0:
        raise ValueError("Family est vide.")
    max_len = len(family[0])
    for sublist in family:
        if len(sublist) != max_len:
            raise ValueError("Toutes les sous-listes dans family doivent avoir la même taille.")
    family_np = np.array(family)# Convertir la liste en tableau NumPy
    if len(set(map(len, family_np))) != 1:
        raise ValueError("Toutes les sous-listes dans family doivent avoir la même taille.")
    print(f"My shape is: {family_np.shape}")# Afficher la forme du tableau original
    new_family_np = family_np[start:end]# Obtenir la sous-liste en utilisant le slicing (positif pars du début et négatif de la fin)
    print(f"My shape is: {new_family_np.shape}")
    return new_family_np.tolist()