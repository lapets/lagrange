from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read().replace(".. include:: toc.rst\n\n", "")

# The lines below can be parsed by `docs/conf.py`.
name = "lagrange"
version = "0.2.0"

setup(
    name=name,
    version=version,
    packages=[name,],
    install_requires=[],
    license="MIT",
    url="https://github.com/lapets/lagrange",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Python library with a basic native implementation "+\
                "of Lagrange interpolation over finite fields.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
