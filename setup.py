import setuptools

from bwh import __author__
from bwh import __email__
from bwh import __title__
from bwh import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="bandwagonhost panel api sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anshengme/bwh",
    packages=setuptools.find_packages(),
    license='LICENSE',
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
