from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "jamescoombes",
    version = "0.0.1",
    author = "James Coombes",
    author_email = "jamespjcoombes@gmail.com",
    description = ("This is the flask app that serves the jamescoombes.com website "
                                   "it was written to invesigate Flask"),
    license = "Not decided",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['app', 'unittests'],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)