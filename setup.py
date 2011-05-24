import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a
# top level
# README file and 2) it's easier to type in the README file than to
# put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "prob",
    version = "0.0.1",
    author = "Matt Jones",
    author_email = "oss@mhjones.org",
    description = ("Utilities for creating and working with discrete"
				   "probability distributions"),
    license = "BSD",
    keywords = "probability",
    url = "http://github.com/nuance/prob",
    packages=['prob'],
    classifiers=[
        "Development Status :: 3 - Alpha",
		"Topic :: Scientific/Engineering :: Mathematics",
		"Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: BSD License",
        ],
    )
