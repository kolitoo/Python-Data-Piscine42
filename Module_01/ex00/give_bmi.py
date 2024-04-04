def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Fonction qui calcule l'imc et la stock dans une liste
    """
    list = []
    for element1, element2 in zip(height, weight):
        IMC = element2 / (element1 * element1)
        list.append(IMC)
    return list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Fonction qui dit si l'imc depasse la limite sous forme
    d'une liste de booléan.
    """
    list = []
    for element in bmi:
        if limit < element:
            bool = True
        else:
            bool = False
        list.append(bool)
    return list
