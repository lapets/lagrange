========
lagrange
========

Python library with a basic native implementation of Lagrange interpolation over finite fields.

.. image:: https://badge.fury.io/py/lagrange.svg
   :target: https://badge.fury.io/py/lagrange
   :alt: PyPI version and link.

Purpose
-------
Native implementation of the Lagrange interpolation algorithm over finite fields.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install lagrange

The library can be imported in the usual way::

    from lagrange import lagrange

Examples
--------
Interpolation can be performed on points represented in a variety of ways::

    >>> lagrange({1: 15, 2: 9, 3: 3}, 17)
    4
    >>> lagrange([(1,15), (2,9), (3,3)], 17)
    4
    >>> lagrange(((1,15), (2,9), (3,3)), 17)
    4
    >>> lagrange({(1,15), (2,9), (3,3)}, 17)
    4
    >>> lagrange([15, 9, 3], 17)
    4
    >>> lagrange(\
        {1: 119182, 2: 11988467, 3: 6052427, 4: 8694701,\
         5: 9050123, 6: 3676518, 7: 558333, 8: 12198248,\
         9: 7344866, 10: 10114014, 11: 2239291, 12: 2515398},\
        15485867)
    123
    >>> lagrange(\
        [119182, 11988467, 6052427, 8694701, 9050123, 3676518,\
         558333, 12198248, 7344866, 10114014, 2239291, 2515398],\
        15485867)
    123

Testing and Conventions
-----------------------
All unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python lagrange/lagrange.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint lagrange
