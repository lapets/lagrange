"""lagrange
https://github.com/lapets/lagrange

Python library with a basic native implementation of Lagrange
interpolation over finite fields.

"""

import doctest


def inv(a, prime):
    """
    Compute multiplicative inverse modulo a prime.
    """
    return pow(a, prime-2, prime)


def interpolate(points, prime):
    """
    Determine the value at x = 0 given a list of pairs.
    If given a list of integers, assumes they are the
    image of the sequence [1, 2, 3, ...].
    """    
    # Compute the Langrange coefficients at 0.
    coefficients = {}
    for i in range(1, len(points)+1):
      coefficients[i] = 1
      for j in range(1, len(points)+1):
        if j != i:
          coefficients[i] = (coefficients[i] * (0-j) * inv(i-j, prime)) % prime

    value = 0
    for i in range(1, len(points)+1):
      value = (value + points[i] * coefficients[i]) % prime

    return value

lagrange = interpolate # Synonym.

if __name__ == "__main__": 
    doctest.testmod()
