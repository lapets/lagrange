from setuptools import setup

with open('README.rst', 'r') as fh:
    long_description = fh.read().replace('.. include:: toc.rst\n\n', '')

# The lines below can be parsed by ``docs/conf.py``.
name = 'lagrange'
version = '1.0.0'

setup(
    name=name,
    version=version,
    packages=[name,],
    install_requires=[],
    extras_require={
        'docs': [
            'sphinx~=4.2.0',
            'sphinx-rtd-theme~=1.0.0'
        ],
        'test': [
            'pytest~=7.0',
            'pytest-cov~=3.0'
        ],
        'lint': [
            'pylint~=2.14.0'
        ],
        'coveralls': [
            'coveralls~=3.3.1'
        ],
        'publish': [
            'setuptools~=62.0',
            'wheel~=0.37',
            'twine~=4.0'
        ]
    },
    license='MIT',
    url='https://github.com/lapets/lagrange',
    author='Andrei Lapets',
    author_email='a@lapets.io',
    description='Python library with a basic native implementation ' + \
                'of Lagrange interpolation over finite fields.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
)
