n = int(input())


def print_rhombus(size):
    for row in range(1, size + 1):
        print(" " * (size - row), end="")
        print("* " * row)

    for row in range(size - 1, 0, -1):
        print(" " * (size - row), end="")
        print("* " * row)


print_rhombus(n)
