from setuptools import setup, find_packages

import pyquantity


__doc__ = """A package to work with physical quantity."""


setup(
	name="PyQuantity",
	version="0.0.2",
	description="A package to work with physical quantity.",
	long_description=__doc__,
	author="LostPy",
	packages=find_packages(),
	url="https://github.com/LostPy/PyQuantity",
	license="MIT",
	classifiers=[
		"Programming Language :: Python",
        "Development Status :: In progress",
        "License :: MIT",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6+"
	],
	include_package_data=True,
	package_data= {'': ['README.md']},
	package_dir={'PyQuantity': './pyquantity'}
)