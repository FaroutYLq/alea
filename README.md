# alea
[![DOI](https://zenodo.org/badge/654100988.svg)](https://zenodo.org/badge/latestdoi/654100988)
[![Test package](https://github.com/XENONnT/alea/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/XENONnT/alea/actions/workflows/pytest.yml)
[![Coverage Status](https://coveralls.io/repos/github/XENONnT/alea/badge.svg?branch=main)](https://coveralls.io/github/XENONnT/alea?branch=main)
[![PyPI version shields.io](https://img.shields.io/pypi/v/alea-inference.svg)](https://pypi.python.org/pypi/alea-inference/)
[![Readthedocs Badge](https://readthedocs.org/projects/alea/badge/?version=latest)](https://alea.readthedocs.io/en/latest/?badge=latest)
[![CodeFactor](https://www.codefactor.io/repository/github/xenonnt/alea/badge)](https://www.codefactor.io/repository/github/xenonnt/alea)

alea is a flexible statistical inference framework. The Python package is designed for constructing, handling, and fitting statistical models, computing confidence intervals and conducting sensitivity studies. It is primarily developed for the [XENONnT dark matter experiment](https://xenonexperiment.org/), but can be used for any statistical inference problem.

If you use alea in your research, please consider citing the software published on [zenodo](https://zenodo.org/badge/latestdoi/654100988).

## Installation
You can install alea from PyPI using pip but **beware that it is listed there as alea-inference!** Thus, you need to run
```
pip install alea-inference
```

For the latest version, you can install directly from the GitHub repository by cloning the repository and running
```
cd alea
pip install .
```
You are now ready to use alea!

## Getting started
The best way to get started is to check out the [documentation](https://alea.readthedocs.io/en/latest/) and have a look at our [tutorial notebooks](https://github.com/XENONnT/alea/tree/main/notebooks). To explore the notebooks interactively, you can use [Binder](https://mybinder.org/v2/gh/XENONnT/alea/HEAD?labpath=notebooks).
## Ackgnowledgements

`alea` is a public package inherited the spirits of previously private XENON likelihood definition and inference construction code `binference` that based on the blueice repo https://github.com/JelleAalbers/blueice.

Binference was developed for XENON1T WIMP searches by Knut Dundas Morå, and for the first XENONnT results by Robert Hammann, Knut Dundas Morå and Tim Wolf.
