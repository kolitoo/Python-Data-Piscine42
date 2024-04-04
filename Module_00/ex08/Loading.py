def ft_tqdm(lst: range) -> None:
    """
    Fonction qui reproduie tqdm
    """
    tot = len(lst)
    barre = ""
    for elem in lst:
        pourcent = int((elem + 1) / tot * 100)
        blocks_nbr = int(pourcent / 5)
        need_spaces = 20 - blocks_nbr
        barre = '##' * blocks_nbr + '  ' * need_spaces
        if pourcent % 2 == 0:
            barre_bar = f"\r{pourcent:3}%|[{barre}] | {(elem + 1):3}/{tot}"
            print(barre_bar, end='', flush=True)
        yield elem
