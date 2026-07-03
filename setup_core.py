from setuptools import setup, find_packages

setup(
    name='ascii-hierarchy-core',
    version='0.1',
    package_dir={"": "ascii_hierarchy"},
    packages=find_packages(where="ascii_hierarchy"),
    install_requires=[]
)