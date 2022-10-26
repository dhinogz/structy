

def intersect(a: list, b: list) -> list:

    set_a =  set(a)
    return [item for item in b if item in set_a]

if __name__ == "__main__":
    a = [1, 2, 5, 7]
    b = [2, 4, 5, 1, 99, 7]

    print(intersect(a, b))
