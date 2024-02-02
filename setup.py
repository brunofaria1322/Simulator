from setuptools import setup, find_packages

setup(
    include_package_data=True,
    name="simulator",
    version="0.0.1",
    description="Simulator for bla bla bla",
    author="Bruno Faria",
    author_email="brunofaria@dei.uc.pt",
    packages=find_packages(),
    install_requires=["networkx", "matplotlib", "geopy"],
    long_description="Simulator for bla bla bla",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
