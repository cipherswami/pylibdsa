from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pylibdsa",
    version="0.1.0",
    author="Aravind Potluri",
    author_email="aravindswami135@gmail.com",
    description="A python based library for Data Structures and Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cipherswami/pylibdsa",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)