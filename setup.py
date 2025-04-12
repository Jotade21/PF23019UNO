from setuptools import setup, find_packages

setup(
    name="PF23019UNO",
    version="1.1",
    author="Josue David Parada Flores",
    author_email="PF23019@ues.edu.sv",
    description="Librería para resolver sistemas lineales y no lineales",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jotade21/PF23019UNO.git",
    packages= ['PF23019UNO'],
    install_requires=[
        'numpy',
    ],
    python_requires='>=3.6',
)