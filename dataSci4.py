import math
from typing import Tuple
from typing import Callable

                        # LINEAR ALGEBRA



# Vectors
Vector = List[float]

# Abstractly, vectors are objects that can be added together to form new vectors and that can be multiplies by scalars (i.e. numbers), also to form new vectors.


def add(v: Vector, w: Vector) -> Vector: #"""Adds corresponding elements""" 
    assert len(v) == len(w), "vectors must be the same length"

return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector: 
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


    # Add more than 2 vectors by index and place result in vector
def vector_sum(vectors: List[Vector]) -> Vector: 
    """Sum all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])

assert all(len(v) == num_elements for v in vectors), "different sizes!"

    #the i-th element of the result is the sum of every vector[i]
return[sum(vector[i] for vector in vectors)]

    for i in range(num_elements)

assert vector_sum([[1, 2], [3, 4], [5, 6], [7,8]]) == [16, 20]



def scalar_multiply(c: float, v: Vector) -> Vector: 
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) === [2, 4, 6] 


def vector_mean(vectors: List[Vector]) -> Vector: """Computes the element-wise average"""
    n = len(vectors)

return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([1,2], [3.4] [5, 6]) == [3, 4]



# Dot Product sum of componentwise products

def dot(v: Vector, w: Vector) -> float:
    '''Computes v_1 * w_1 + ... + v_n * w_n'''
    assert len(v) == len(w), "vectors must be same length"

return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32 

# The dot product is like saying the length of the vector you'd get if you projected v onto w (or in the w direction)



# Vectors are lists (arrays) with dynamic length allowing different functions to be performed on them elegantly. The one below squares all the numbers in a given list individually then sums the squares collectively and stores it with size "float".
def sum_of_squares(v: Vector) -> float: 
    """Returns v_1 * v_1 + ... + v_n * v_n""" 
    return dot(v, v)

assert sum_of_swuares([1, 2, 3]) == 14     # 2 + 4 + 9


# returns c for a^2 + b^2 = c^2
def magnitude(v: Vector) _> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4,]) == 5



# define distance between two vectors that do not touch
# sqrt((v1 - w1)^2 + ... + (vn - wn)^2))
def squared_distance(v: Vector, w: Vector) -> float: 
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float: 
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))


# Vectors are good for exposition but not for performance. Production code will use the NumPy library.





                            # Matrices 

# Matrix is a two dimensional collection of numbers. Represented as lists of lists. Inner = row.

Matrix = List[List[float]]

A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2], [4, 5], [5, 6]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0])

    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3) # 2 rows, 3 columns


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]    # A[i] is already the ith row

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]     # jth element of row A_i
        for A_i in A]



# Create a matrix given its shape (lenA - rows, lenA[0] - col) and a function for generating elements. Use nested list comprehension.
def make_matrix(num_rows: int, num_cols: int,
entry_fn: Callable[[int, int], float]) -> Matrix:

    """ Returns a num_rows x num_cols matrix whose (i, j)-th entry is entry_fn(i,j)"""

    return [[entry_fn(i, j)
    # give i, create a list
        for j in range(num_cols)]   # [entry_fn(i, 0), ...]
            for i in range(num_rows)]   # create one list for each i
    

# Using this function create a 5x5 identity matrix(with 1s on diagonal and 0s elsewhere.)
def identity_matrix(n: int) -> Matrix: 
    """Returns the n x n identity matrix"""

    return make_matrix(n, n, lambda i, j: 1 if == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0]], 
[0, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 1]

