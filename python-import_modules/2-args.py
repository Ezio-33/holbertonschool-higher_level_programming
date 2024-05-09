#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    print(len(argv) - 1, "arguments", end='')
    if len(argv) == 1:
        print(".", end='')
    else:
        print(":", end='')
    print()
    if len(argv) > 1:
        for i in range(1, len(argv)):
            print(i, ':', argv[i])
