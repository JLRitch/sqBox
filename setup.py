import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

description = (
    '''This is an example package to aid with learning how to build packages.
    It makes use of a Square object, which can actually be a rectangle as well (doh!).
    '''
)

setuptools.setup(
    name="sqBox",
    version="0.0.0",
    author="Jere Ritchie<jereritchie@gmail.com>",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JLRitch/sqBox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    license="MIT"
)