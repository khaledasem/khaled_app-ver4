from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in khaled_app/__init__.py
from khaled_app import __version__ as version

setup(
	name="khaled_app",
	version=version,
	description="a",
	author="khaled asem",
	author_email="yemenlion2020@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
