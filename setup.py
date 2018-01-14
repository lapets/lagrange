from setuptools import setup

setup(
    name             = 'lagrange',
    version          = '0.1.0.0',
    packages         = ['lagrange',],
    install_requires = [],
    license          = 'MIT',
    url              = 'https://github.com/lapets/lagrange',
    author           = 'Andrei Lapets',
    author_email     = 'a@lapets.io',
    description      = 'Python library with a basic native implementation of Lagrange interpolation over finite fields.',
    long_description = open('README.rst').read(),
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
)
