#!/usr/bin/python3

for nombre in range(100):
    if nombre < 99:
        print("{:02d}, ".format(nombre), end="")
    else:
        print("{:02d}".format(nombre))
