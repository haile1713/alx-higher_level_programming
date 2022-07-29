>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

>>> matrixA = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
>>> matrixB = [[1, 2, 3], [4, 5, 6]]

>>> print(matrix_divided(matrixA, 4))
[[0.25, 0.5, 0.75], [0.75, 1.0, 1.25], [1.25, 1.5, 1.75]]
>>> print(matrix_divided(matrixB, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

error input
>>> noneL = None
>>> empty_list = []
>>> empty_lists = [[], [], []]
>>> not_list = [42, [2, 5], [1, 2, 3]]
>>> not_all_num = [["blue", 1, 2], [3, 4, "f"], ["23b", 5, 6]]
>>> diff_len = [[1,3,3,3], [3,5,1,2,5], [2,5,8]]

>>> matrix_divided(noneL, 3)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided(empty_list, 2)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided(empty_lists, 3)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided(not_list, 2)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided(not_all_num, 2)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> print(matrix_divided(matrixA, 0))
Traceback (most recent call last):
ZeroDivisionError: division by zero

>>> matrix_divided(diff_len, 3)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size
