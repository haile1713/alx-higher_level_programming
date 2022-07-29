>>> print_square = __import__('4-print_square').print_square

>>> print_square(3)
xxx
xxx
xxx

>>> print_square(1)
x

>>> print_square(2)
xx
xx

>>> print_square(-1)
Traceback (most recent call last):
ValueError: size must be >= 0

>>> print_square("idk")
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square(4.0)
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square('42')
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square()
Traceback (most recent call last):
TypeError: print_square() missing 1 required positional argument: 'size'

>>> print_square(1, 2)
Traceback (most recent call last):
TypeError: print_square() takes 1 positional argument but 2 were given

>>> print_square(0)
