from setuptools import setup, find_packages

setup(
    name="padlock_validation",
    version="v0.1",
    url="https://github.com/AlexBecalick/padlock_validation/", 
    license="MIT",
    author="Alex Becalick",
    author_email="alexander.becalick@crick.ac.uk",
    description="Code for checking padlock specificity",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "matplotlib",
        "natsort",
        "pandas",
        "tqdm",
        "mygene",
    ]
)