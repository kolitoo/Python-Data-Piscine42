def ft_filter(function, iterable):
    """
    reproduction de la fonction filter(). Elle retourne un iterateur
    où les elements de iterable ont été filtrer par la fonction
    """
    newlist = []
    for item in iterable:
        if function(item):
            newlist.append(item)
    return newlist
