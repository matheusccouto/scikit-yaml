"""Setup Python package."""

import os
import setuptools

THIS_DIR = os.path.dirname(__file__)

with open(os.path.join(THIS_DIR, "requirements.txt"), encoding="utf-8") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="scikit-yaml",
    version="0.2.1",
    author="Matheus Couto",
    author_email="matheusccouto@gmail.com",
    description="Define Scikit-Learn objects using YAML",
    packages=["skyaml"],
    install_requires=required,
)
