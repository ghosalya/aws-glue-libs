from setuptools import setup, find_packages

setup(
    name="awsglue",
    install_requires=["pyspark"],
    packages=find_packages(exclude=["tests_*"])
)
