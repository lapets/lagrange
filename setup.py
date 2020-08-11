from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="lagrange",
    version="0.2.0",
    packages=["lagrange",],
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
