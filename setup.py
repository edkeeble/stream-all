"""stream-all: stream all the files"""

from setuptools import find_namespace_packages, setup
from version import __version__

with open("README.md") as f:
    desc = f.read()


install_requires = ["stream-zip"]

extra_reqs = {
    "dev": ["black==22.3.0", "flake8==4.0.1", "pyright==1.1.299"],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
    "server": ["fastapi", "uvicorn[standard]", "fire"],
}


setup(
    name="stream-all",
    description=("A library for streaming an arbitrary collection of files."),
    long_description=desc,
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="stream fastapi stream-zip zip",
    author="Edward Keeble",
    author_email="edw@rdak.ca",
    url="https://github.com/edkeeble/stream-all",
    license="MIT",
    packages=find_namespace_packages(exclude=["tests", "scripts"]),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
    scripts=["scripts/streamall"],
    version=__version__,  # type: ignore
)
