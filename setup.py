from os import path
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="ezapi_tmdb",
    keywords="TMDb",
    version="0.4.0",
    packages=find_packages(),
    description="An Python wrapper for TMDb API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zehengl/ezapi_tmdb",
    author="Zeheng Li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng Li",
    maintainer_email="imzehengl@gmail.com",
    license="MIT",
    install_requires=["requests", "wrapt"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
