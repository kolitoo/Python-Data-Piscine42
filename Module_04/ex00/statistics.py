from typing import Any


def find_mean(args, i):
    """"""
    result = sum(args) / len(args)
    if i == 1:
        print(f"mean : {result}")
    return result


def find_median(args):
    """"""
    if len(args) % 2 == 1:
        result = args[len(args) // 2 - 1]  # div entière
    else:
        sorted_args = tuple(sorted(args))
        mid_right = len(sorted_args) // 2
        mid_left = mid_right - 1
        result = (sorted_args[mid_left] + sorted_args[mid_right]) / 2
    print(f"median : {result}")


def find_quartile(args):
    """"""
    sorted_args = tuple(sorted(args))
    n = len(sorted_args)
    q1_index = n // 4
    q3_index = 3 * q1_index

    q1 = sorted_args[q1_index]
    q3 = sorted_args[q3_index]
    print(f"quartile : [{q1}, {q3}]")


def find_std_or_var(args, i):
    """"""
    moyenne = find_mean(args, 0)
    sous_moy = []
    result = 0
    for x in range(len(args)):
        sous_moy.append(moyenne - args[x])
    for x in range(len(sous_moy)):
        result += (sous_moy[x] ** 2)
    result = (result / len(args) - 1)
    if i == 0:
        print(f"var : {result}")
    else:
        print(f"std : {result ** 0.5}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """"""
    if len(args) == 0:
        print("Error")
        return
    for key, value in kwargs.items():
        if value == "mean":
            find_mean(args, 1)
        elif value == "median":
            find_median(args)
        elif value == "quartile":
            find_quartile(args)
        elif value == "std":
            find_std_or_var(args, 1)
        elif value == "var":
            find_std_or_var(args, 0)
        else:
            print("Error")
