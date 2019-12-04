from cs50 import get_int

h = get_int("Height: ")

for i in range(h):
    print(" " * (h - i - 1) + "#" * (i + 1))

