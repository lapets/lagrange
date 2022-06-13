========
lagrange
========

Library with a basic, pure Python implementation of Lagrange interpolation over finite fields.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/lagrange.svg
   :target: https://badge.fury.io/py/lagrange
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/lagrange/badge/?version=latest
   :target: https://lagrange.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/lagrange/actions/workflows/lint-test-cover-docs.yml/badge.svg
   :target: https://github.com/lapets/lagrange/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/lagrange/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/lagrange?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------
Pure Python implementation of the `Lagrange interpolation <https://en.wikipedia.org/wiki/Lagrange_polynomial>`__ algorithm over finite fields.

Package Installation and Usage
------------------------------
This library is available as a `package on PyPI <https://pypi.org/project/lagrange>`__::

    python -m pip install lagrange

The library can be imported in the usual way::

    from lagrange import lagrange

Examples
--------
Interpolation can be performed on collections of points represented in a variety of ways::

    >>> lagrange({1: 15, 2: 9, 3: 3}, 17)
    4
    >>> lagrange([(1, 15), (2, 9), (3, 3)], 17)
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

Development
-----------
All installation and development dependencies are managed using `setuptools <https://pypi.org/project/setuptools>`__ and are fully specified in ``setup.py``. The ``extras_require`` parameter is used to `specify optional requirements <https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
.. include:: toc.rst

The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__::

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. ../setup.py && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see ``setup.cfg`` for configuration details)::

    python -m pip install .[test]
    nosetests --cover-erase

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python lagrange/lagrange.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org>`__::

    python -m pip install .[lint]
    pylint lagrange

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/lagrange>`__ for this library.

Versioning
^^^^^^^^^^
Beginning with version 0.2.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/lagrange>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Remove any old build/distribution files. Then, package the source into a distribution archive using the `wheel <https://pypi.org/project/wheel>`__ package::

    rm -rf dist *.egg-info
    python setup.py sdist bdist_wheel

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__ using the `twine <https://pypi.org/project/twine>`__ package::

    python -m twine upload dist/*
