"""Setup Python package."""

import setuptools

with open("requirements.txt", encoding="utf-8") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="skyaml",
    version="0.1.0",
    author="Matheus Couto",
    author_email="matheusccouto@gmail.com",
    description="Define Scikit-Learn objects using YAML",
    packages=["skyaml"],
    install_requires=required,
)
