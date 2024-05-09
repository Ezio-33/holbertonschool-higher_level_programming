#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nombre_arg = len(sys.argv) - 1

    if nombre_arg == 0:
        print("{} arguments.".format(nombre_arg))
    elif nombre_arg == 1:
        print("{} argument:".format(nombre_arg))
    else:
        print("{} arguments:".format(nombre_arg))

    if nombre_arg >= 1:
        nombre_arg = 0
        for arg in sys.argv:
            if nombre_arg != 0:
                print("{}: {}".format(nombre_arg, arg))
            nombre_arg += 1
