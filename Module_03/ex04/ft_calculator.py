class calculator:
    """"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """"""
        result = sum(V1[x] * V2[x] for x in range(len(V1)))
        print(f"Dot product is : {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """"""
        result = [float(V1[x] + V2[x]) for x in range(len(V1))]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """"""
        result = [float(V1[x] - V2[x]) for x in range(len(V1))]
        print(f"Sous Vector is : {result}")
