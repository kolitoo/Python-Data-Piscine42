def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** 1.5


def outer(x: int | float, function) -> object:
    def inner() -> float:
