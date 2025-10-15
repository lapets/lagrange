========
lagrange
========

Pure-Python implementation of Lagrange interpolation over finite fields.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/lagrange.svg#
   :target: https://badge.fury.io/py/lagrange
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/lagrange/badge/?version=latest
   :target: https://lagrange.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/lagrange/workflows/lint-test-cover-docs/badge.svg#
   :target: https://github.com/lapets/lagrange/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/lagrange/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/lagrange?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------
This library provides a pure-Python implementation of the `Lagrange interpolation <https://en.wikipedia.org/wiki/Lagrange_polynomial>`__ algorithm over finite fields.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/lagrange>`__:

.. code-block:: bash

    python -m pip install lagrange

The library can be imported in the usual manner:

.. code-block:: python

    from lagrange import lagrange

Examples
^^^^^^^^
Interpolation can be performed on collections of points represented in a variety of ways:

.. code-block:: python

    >>> lagrange({1: 15, 2: 9, 3: 3}, 17)
    4
    >>> lagrange([(1, 15), (2, 9), (3, 3)], 17)
    4
    >>> lagrange([15, 9, 3], 17)
    4
    >>> lagrange(
    ...     {
    ...         1: 119182, 2: 11988467, 3: 6052427, 4: 8694701,
    ...         5: 9050123, 6: 3676518, 7: 558333, 8: 12198248,
    ...         9: 7344866, 10: 10114014, 11: 2239291, 12: 2515398
    ...     },
    ...     15485867
    ... )
    123
    >>> lagrange(
    ...     [
    ...         119182, 11988467, 6052427, 8694701, 9050123, 3676518,
    ...         558333, 12198248, 7344866, 10114014, 2239291, 2515398
    ...     ],
    ...     15485867
    ... )
    123

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__:

.. code-block:: bash

    python -m pip install ".[docs,lint]"

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__:

.. code-block:: bash

    python -m pip install ".[docs]"
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details):

.. code-block:: bash

    python -m pip install ".[test]"
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__:

.. code-block:: bash

    python src/lagrange/lagrange.py -v

Style conventions are enforced using `Pylint <https://pylint.readthedocs.io>`__:

.. code-block:: bash

    python -m pip install ".[lint]"
    python -m pylint src/lagrange

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/lagrange>`__ for this library.

Versioning
^^^^^^^^^^
Beginning with version 0.2.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/lagrange>`__ via the GitHub Actions workflow found in ``.github/workflows/build-publish-sign-release.yml`` that follows the `recommendations found in the Python Packaging User Guide <https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`__.

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions.

To publish the package, create and push a tag for the version being published (replacing ``?.?.?`` with the version number):

.. code-block:: bash

    git tag ?.?.?
    git push origin ?.?.?
