#!/usr/bin/python3
for nombre_1 in range(10):
    for nombre_2 in range(nombre_1 + 1, 10):
        print("{:d}{:d}".format(nombre_1, nombre_2), end="")
        if nombre_1 != 8 or nombre_2 != 9:
            print(", ", end="")
print()
