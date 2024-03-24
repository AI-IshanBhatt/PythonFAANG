def is_ugly(n):

    if n == 0:
        return False

    while n%2 == 0:
        n //= 2

    while n%3 == 0:
        n //= 3

    while n%5 == 0:
        n //= 5

    return n == 1


if __name__ == "__main__":
    print(is_ugly(28))
    print(is_ugly(30))
    print(is_ugly(35))