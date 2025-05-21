from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="WatchtowerOps",
    version="0.1",
    author="Sahil Rahate",
    packages=find_packages(),
    install_requires = requirements,
)