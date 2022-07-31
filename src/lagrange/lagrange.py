"""
Pure-Python implementation of Lagrange interpolation over finite fields.
"""
from __future__ import annotations
from functools import reduce
from typing import Union, Optional, Sequence, Iterable
import doctest
import collections.abc
import itertools

def _inv(a: int, prime: int) -> int:
    """
    Compute multiplicative inverse modulo a prime.
    """
    return pow(a, prime - 2, prime)

def interpolate(
        points: Union[dict, Sequence[int], Iterable[Sequence[int]]],
        modulus: int,
        degree: Optional[int] = None
    ) -> int:
    """
    Determine the value at the origin of the domain (*e.g.*, where *x* = 0)
    given a collection of points. The point information can be represented as
    a collection of two-component coordinates, as a dictionary, or as a sequence
    of values.

    :param points: Collection of points to interpolate.
    :param modulus: Modulus representing the finite field within which to interpolate.
    :param degree: Degree of the target polynomial.

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

    If the point information is supplied as an |Iterable|_ of integers, that
    iterable object must be a |Sequence|_.

    >>> interpolate({15, 9, 3}, 17)
    Traceback (most recent call last):
      ...
    TypeError: iterable of integers that represents points must be a sequence

    Alternatively, a two-coordinate |Sequence|_ can be used to represent each
    individual point. In that case, any |Iterable|_ of such individual points
    is supported.

    >>> interpolate({(1, 15), (2, 9), (3, 3)}, 17)
    4

    This function is able to interpolate when supplied more points than
    necessary (*i.e.*, given the degree).

    >>> lagrange({1: 4, 2: 6, 3: 8, 4: 10, 5: 12}, modulus=65537)
    2
    >>> lagrange({1: 4, 2: 6, 3: 8, 4: 10, 5: 12}, degree=4, modulus=65537)
    2
    >>> lagrange({1: 4, 2: 6, 3: 8, 4: 10, 5: 12}, degree=5, modulus=65537)
    Traceback (most recent call last):
      ...
    ValueError: not enough points for a unique interpolation
    >>> lagrange({1: 4, 2: 6, 3: 8, 4: 10, 5: 12}, degree=1, modulus=65537)
    2
    >>> lagrange({49: 200, 5: 24, 3: 16}, degree=2, modulus=65537)
    4
    >>> lagrange({49: 200, 5: 24, 3: 16}, degree=1, modulus=65537)
    4
    >>> lagrange({1: 16, 2: 25, 3: 36}, degree=1, modulus=65537)
    7
    >>> lagrange({3: 36, 1: 16, 2: 25}, degree=1, modulus=65537)
    6
    >>> lagrange({1: 16, 2: 25, 3: 36}, degree=2, modulus=65537)
    9
    >>> lagrange({3: 36, 1: 16, 2: 25}, degree=2, modulus=65537)
    9
    >>> lagrange({5: 64, 2: 25, 3: 36}, degree=2, modulus=65537)
    9

    Interpolation in trivial scenarios is supported, as well.

    >>> lagrange([12345], degree=0, modulus=65537)
    12345

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
    >>> interpolate([15, 9, 3], 17, 'abc')
    Traceback (most recent call last):
      ...
    TypeError: expecting an integer degree
    >>> interpolate([15, 9, 3], 17, -3)
    Traceback (most recent call last):
      ...
    ValueError: expecting a nonnegative integer degree
    """
    # pylint: disable=too-many-branches # Allow large number of branches for type checking.
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

    elif isinstance(points, collections.abc.Iterable):
        is_sequence = isinstance(points, collections.abc.Sequence) # If iterable contains integers.
        entries = list(points)

        if all(isinstance(e, int) for e in entries):
            if not is_sequence:
                raise TypeError(
                    'iterable of integers that represents points must be a sequence'
                )

            values = dict(zip(range(1, len(entries) + 1), entries)) # Valid representation.

        elif all(isinstance(e, collections.abc.Sequence) for e in entries):
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

    if not isinstance(modulus, int):
        raise TypeError('expecting an integer prime modulus')

    if modulus <= 1:
        raise ValueError('expecting a positive integer prime modulus')

    if degree is not None:
        if not isinstance(degree, int):
            raise TypeError('expecting an integer degree')

        if degree < 0:
            raise ValueError('expecting a nonnegative integer degree')

    degree = degree or len(points) - 1

    if len(values) <= degree:
        raise ValueError('not enough points for a unique interpolation')

    # Restrict the set of points used in the interpolation.
    xs = list(values.keys())[:degree + 1]

    # Field arithmetic helper functions.
    mul = lambda a, b: (a % modulus) * b % modulus # pylint: disable=unnecessary-lambda-assignment
    div = lambda a, b: mul(a, _inv(b, modulus)) # pylint: disable=unnecessary-lambda-assignment

    # Compute the value of each unique Lagrange basis polynomial at ``0``,
    # then sum them all up to get the resulting value at ``0``.
    return sum(
        reduce(
            mul,
            itertools.chain([values[x]], (
                # Extrapolate using the fact that *y* = ``1`` if
                # ``x`` = ``x_known``, and *y* = ``0`` for the other
                # known values in the domain.
                div(0 - x_known, x - x_known)
                for x_known in xs if x_known is not x
            )),
            1
        )
        for x in xs
    ) % modulus

lagrange = interpolate
"""
Alias for :obj:`interpolate`.
"""

if __name__ == '__main__':
    doctest.testmod() # pragma: no cover
