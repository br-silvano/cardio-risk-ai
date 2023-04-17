from setuptools import setup, find_packages

setup(
    name="cardio-risk",
    version="0.1",
    author="Silvano Souza",
    author_email="",
    description="Module for sharing code among different microservices",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
