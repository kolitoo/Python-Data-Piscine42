import sys
from ft_filter import ft_filter


def check_len(S, N) -> bool:
    return len(S) > N


def main(args):
    """

    """
    if len(args) != 3:
        raise AssertionError("AssertionError: the arguments are bad")
    try:
        S = str(args[1])
        N = int(args[2])
    except ValueError:
        print("First argument: string, second argument: int")
    Base_list = []
    world = ""
    for i in range(len(S)):
        if S[i].isspace():
            if i != 0:
                Base_list.append(world)
                world = ""
            continue
        world += S[i]
    if world != "":
        Base_list.append(world)
    # print(Base_list)
    Final_list = ft_filter(lambda x: check_len(x, N), Base_list)
    print(Final_list)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
