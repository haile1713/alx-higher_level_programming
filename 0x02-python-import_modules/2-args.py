#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    arglen = len(argv) - 1
    if arglen == 0:
        print('0 arguments.')
    elif arglen == 1:
        print('1 argument:')
        print('1: {}'.format(argv[1]))
    else:
        print('{} arguments:'.format(arglen))
        for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))
