from typing import Tuple


def key_fun(tup: Tuple[str, int]):
    return tup[1]


def main():
    list_a = [
        ("z", 5),
        ("z", 3),
        ("c", 6),
        ("a", 1),
        ("m", 11),
        ("k", 5),
        ("l", 8),
        ("k", 4),
    ]

    # FILL IN BELOW
    sorted()
    # END FILL IN

    print(list_a)
    assert list_a == [('a', 1), ('z', 3), ('k', 4), ('z', 5), ('k', 5), ('c', 6), ('l', 8), ('m', 11)]


main()