from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ezapi_tmdb',
    keywords='TMDb v3 v4',
    version='0.2.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
    description='An Python wrapper for TMDb API',
    long_description=long_description,

    url='https://github.com/zehengl/ezapi_tmdb',

    author='Zeheng Li',
    author_email='imzehengl@gmail.com',

    license='MIT',

    entry_points={
        'console_scripts': [
            'tmdb3 = tmdb.cli.v3:run',
            'tmdb4 = tmdb.cli.v4:run',
        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],


    install_requires=[
        'click',
        'configparser',
        'requests',
        'six',
    ],

    test_suite='tests',
)
