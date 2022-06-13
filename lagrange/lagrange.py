"""
Python library with a basic native implementation of Lagrange
interpolation over finite fields.
"""
from __future__ import annotations
from typing import Union
from collections.abc import Iterable, Sequence
import doctest

def _inv(a, prime):
    """
    Compute multiplicative inverse modulo a prime.
    """
    return pow(a, prime - 2, prime)

def interpolate(
        points: Union[dict, Sequence[int], Iterable[Sequence[int]]], prime: int
    ) -> int:
    # pylint: disable=R0912 # Accommodate large number of branches for type checking.
    """
    Determine the value at the origin of the domain (*e.g.*, where *x* = 0)
    given a collection of points. The point information can be represented as
    a collection of two-component coordinates, as a dictionary, or as a sequence
    of values.

    >>> interpolate([(1, 15), (2, 9), (3, 3)], 17)
    4
    >>> interpolate({1: 15, 2: 9, 3: 3}, 17)
    4
    >>> interpolate(
    ...     {
    ...         1: 119182, 2: 11988467, 3: 6052427, 4: 8694701,
    ...         5: 9050123, 6: 3676518, 7: 558333, 8: 12198248,
    ...         9: 7344866, 10: 10114014, 11: 2239291, 12: 2515398
    ...     },
    ...     15485867
    ... )
    123

    If a list of integers is supplied, it is assumed that they are
    the image of the sequence ``[1, 2, 3, ...]``.

    >>> interpolate([15, 9, 3], 17)
    4
    >>> interpolate(
    ...     [
    ...         119182, 11988467, 6052427, 8694701, 9050123, 3676518,
    ...         558333, 12198248, 7344866, 10114014, 2239291, 2515398
    ...     ],
    ...     15485867
    ... )
    123

    .. |Iterable| replace:: ``Iterable``
    .. _Iterable: https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable

    .. |Sequence| replace:: ``Sequence``
    .. _Sequence: https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence

    If the point information is supplied as an |Iterable| of integers, that iterable
    must be a |Sequence|_.

    >>> interpolate({15, 9, 3}, 17)
    Traceback (most recent call last):
      ...
    TypeError: iterable of integers that represents points must be a sequence

    Alternatively, a two-coordinate |Sequence|_ can be used to represent each individual point.
    In that case, any |Iterable|_ of such individual points is supported.

    >>> interpolate({(1, 15), (2, 9), (3, 3)}, 17)
    4

    At least one point must be supplied.

    >>> interpolate([], 17)
    Traceback (most recent call last):
      ...
    ValueError: at least one point is required

    An exception is raised if a supplied argument (or a component thereof) does not
    have the expected structure or is not of the expected type.

    >>> interpolate({1: 15.0, 'a': 9, 'b': 3}, 17)
    Traceback (most recent call last):
      ...
    TypeError: dictionary that represents points must have integer keys and values
    >>> interpolate({(1, 15, 0), (2, 9, 0), (3, 3, 0)}, 17)
    Traceback (most recent call last):
      ...
    TypeError: iterable that represents points must contain integers or two-element \
sequences of integers
    >>> interpolate('abc', 123)
    Traceback (most recent call last):
      ...
    TypeError: iterable that represents points must contain integers or two-element \
sequences of integers
    >>> interpolate(1.23, 123)
    Traceback (most recent call last):
      ...
    TypeError: expecting dictionary or iterable that represents points
    >>> interpolate([15, 9, 3], 'abc')
    Traceback (most recent call last):
      ...
    TypeError: expecting an integer prime modulus
    >>> interpolate([15, 9, 3], -17)
    Traceback (most recent call last):
      ...
    ValueError: expecting a positive integer prime modulus
    """
    values = None # Initially, assume that the supplied point data is not valid.

    if isinstance(points, dict):
        if not (
            all(isinstance(k, int) for k in points.keys()) and \
            all(isinstance(v, int) for v in points.values())
        ):
            raise TypeError(
                'dictionary that represents points must have integer keys and values'
            )

        values = points # Valid representation.

    elif isinstance(points, Iterable):
        is_sequence = isinstance(points, Sequence) # In case iterable contains only integers.
        entries = list(points)

        if all(isinstance(e, int) for e in entries):
            if not is_sequence:
                raise TypeError(
                    'iterable of integers that represents points must be a sequence'
                )

            values = dict(zip(range(1, len(entries) + 1), entries)) # Valid representation.

        elif all(isinstance(e, Sequence) for e in entries):
            entries = [tuple(e) for e in entries]
            if not all(
                len(e) == 2 and all(isinstance(c, int) for c in e)
                for e in entries
            ):
                raise TypeError(
                    'iterable that represents points must contain integers ' + \
                    'or two-element sequences of integers'
                )

            values = dict(entries) # Valid representation.

    if values is None:
        raise TypeError('expecting dictionary or iterable that represents points')

    if len(values) == 0:
        raise ValueError('at least one point is required')

    if not isinstance(prime, int):
        raise TypeError('expecting an integer prime modulus')

    if prime <= 1:
        raise ValueError('expecting a positive integer prime modulus')

    # Compute the Lagrange coefficients at ``0``.
    coefficients = {}
    for i in range(1, len(values) + 1):
        coefficients[i] = 1
        for j in range(1, len(values) + 1):
            if j != i:
                coefficients[i] = (coefficients[i] * (0 - j) * _inv(i - j, prime)) % prime

    value = 0
    for i in range(1, len(values) + 1):
        value = (value + values[i] * coefficients[i]) % prime

    return value

lagrange = interpolate
"""
Alias for :obj:`interpolate`.
"""

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
