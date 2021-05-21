import os.path
import sys

from setuptools import find_packages, setup

setupdir = os.path.dirname(__file__)

for line in open(os.path.join(setupdir, "packaging_experiment.py")).read().splitlines():
    if line.startswith("__version__"):
        version = line.split('"')[1]
        break
else:
    raise RuntimeError("Unable to find version string.")

requirements = []
for line in open(os.path.join(setupdir, "requirements.txt"), encoding="ASCII"):
    if line.strip() and not line.startswith("#"):
        requirements.append(line)

with open(os.path.join(setupdir, "README.rst")) as fp:
    long_description = fp.read()

setup(
    name="mp_packaging_experiment",
    version=version,
    description="Experiment for packaging for MicroPython",
    long_description=long_description,
    url="https://github.com/aivarannamaa/packaging_experiment",
    author="Aivar Annamaa",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "Topic :: Software Development",
    ],
    keywords="MicroPython CircuitPython pip upip",
    project_urls={
        "Source code": "https://github.com/aivarannamaa/packaging_experiment",
        "Bug tracker": "https://github.com/aivarannamaa/packaging_experiment/issues",
    },
    platforms=["Windows", "macOS", "Linux", "MicroPython", "CircuitPython"],
    install_requires=requirements,
    py_modules=["packaging_experiment"],
    entry_points={"console_scripts": ["packaging_experiment = packaging_experiment:main"]},
)
