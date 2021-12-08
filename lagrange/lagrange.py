"""
Python library with a basic native implementation of Lagrange
interpolation over finite fields.
"""
import doctest

def _inv(a, prime):
    """
    Compute multiplicative inverse modulo a prime.
    """
    return pow(a, prime - 2, prime)

def interpolate(points, prime):
    """
    Determine the value at ``x = 0`` given a list of pairs or a
    dictionary mapping indices to values.

    >>> interpolate({1: 15, 2: 9, 3: 3}, 17)
    4
    >>> interpolate([(1, 15), (2, 9), (3, 3)], 17)
    4
    >>> interpolate([15, 9, 3], 17)
    4

    If a list of integers is supplied, it is assumed that they are
    the image of the sequence ``[1, 2, 3, ...]``.

    >>> interpolate(\
        {1: 119182, 2: 11988467, 3: 6052427, 4: 8694701,\
         5: 9050123, 6: 3676518, 7: 558333, 8: 12198248,\
         9: 7344866, 10: 10114014, 11: 2239291, 12: 2515398},\
        15485867)
    123
    >>> interpolate(\
        [119182, 11988467, 6052427, 8694701, 9050123, 3676518,\
         558333, 12198248, 7344866, 10114014, 2239291, 2515398],\
        15485867)
    123

    Exceptions are raised if the supplied arguments are not of the
    expected types.

    >>> interpolate('abc', 123)
    Traceback (most recent call last):
      ...
    TypeError: expecting a list of values, list of points, or a dictionary
    >>> interpolate([15, 9, 3], 'abc')
    Traceback (most recent call last):
      ...
    ValueError: expecting an integer prime modulus
    >>> interpolate([15, 9, 3], -17)
    Traceback (most recent call last):
      ...
    ValueError: expecting a positive integer prime modulus
    """
    if isinstance(points, list) and all(isinstance(p, int) for p in points):
        points = dict(zip(range(1, len(points) + 1), points))
    elif isinstance(points, (list, set, tuple)) and\
       len(points) > 0 and\
       all(isinstance(p, (list, tuple)) and len(p) == 2 for p in points):
        points = dict([tuple(p) for p in points])
    elif isinstance(points, dict):
        pass
    else:
        raise TypeError("expecting a list of values, list of points, or a dictionary")

    if not isinstance(prime, int):
        raise ValueError("expecting an integer prime modulus")

    if prime <= 1:
        raise ValueError("expecting a positive integer prime modulus")

    # Compute the Lagrange coefficients at ``0``.
    coefficients = {}
    for i in range(1, len(points) + 1):
        coefficients[i] = 1
        for j in range(1, len(points) + 1):
            if j != i:
                coefficients[i] = (coefficients[i] * (0-j) * _inv(i-j, prime)) % prime

    value = 0
    for i in range(1, len(points)+1):
        value = (value + points[i] * coefficients[i]) % prime

    return value

lagrange = interpolate # Synonym.

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
