from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="newscompiler",
    version="0.2.0",
    description="A simple wrapper tool to run scripts easily from CLI.",
    long_description=readme,
    author="Cauã Bernardino",
    author_email="",
    url="https://github.com/cauabernardino/newscompiler",
    install_requires=REQUIREMENTS,
    license=license,
    packages=find_packages(exclude=("tests")),
    entry_points={
        "console_scripts": [
            "news = newscompiler.main:main",
        ],
    },
)
