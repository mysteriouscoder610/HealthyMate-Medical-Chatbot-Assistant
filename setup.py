from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Ayush Jha",
    author_email="jha2004ayush@gmail.com",
    packages=find_packages(),
    install_requires=[]
)

# setup.py is used to make this project an installable Python package.
# It allows `pip install .`, auto-discovers modules with find_packages(),
# and installs dependencies listed in install_requires. Required if the
# project will be reused, shared, deployed, or published to PyPI.