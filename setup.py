"""Python setup.py for mars_sre_runbook_api package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("mars_sre_runbook_api", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="mars_sre_runbook_api",
    version=read("mars_sre_runbook_api", "VERSION"),
    description="Awesome mars_sre_runbook_api created by SamuelWitke",
    url="https://github.com/SamuelWitke/mars_sre_runbook_api/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="SamuelWitke",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["mars_sre_runbook_api = mars_sre_runbook_api.__main__:main"]
    },
    extras_require={
        "test": read_requirements("requirements-test.txt")
        + read_requirements("requirements-base.txt")
    },
)
