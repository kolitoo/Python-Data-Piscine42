class calculator:
    """"""
    def __init__(self, object):
        self.vector = object

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            if object == 0:
                raise ZeroDivisionError("Impossible operation.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
