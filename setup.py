import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="positionkey",
    version="0.0.1",
    description="Mouse clicks(GUI) mapped to keypresses",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/niteshctrl/positionkey",
    author="Nitesh Prasad",
    author_email="nitesh1612@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pyautogui==0.9.53', 'pynput==1.6.7']
)