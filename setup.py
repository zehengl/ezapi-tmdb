from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="ezapi_tmdb",
    keywords="TMDb",
    version="0.8.1",
    packages=["tmdb"],
    description="A Python wrapper for TMDb API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zehengl/ezapi-tmdb",
    author="Zeheng Li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng Li",
    maintainer_email="imzehengl@gmail.com",
    license="MIT",
    install_requires=requirements,
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
        "python-dotenv",
        "seleniumbase",
    ],
    test_suite="tests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
