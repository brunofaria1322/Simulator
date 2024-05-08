[comment]: # "TODO: Change the links below! Change everything that has simulator to the decided name"

# Overview

[![Documentation Status](https://readthedocs.org/projects/simulator/badge/?version=latest)](https://simulator.readthedocs.io/en/latest/?badge=latest)

[![GitHub license](https://img.shields.io/github/license/brunofaria1322/Simulator)](https://github.com/brunofaria1322/Simulator/blob/main/LICENSE)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)
[![PyPI version](https://badge.fury.io/py/Simulator.svg)](https://badge.fury.io/py/Simulator)

brief description about the simulator ... bla bla bla

## Installation

Install the package using pip:

```bash
pip install <name_not_defined_yet>
```

## Documentation

The documentation is available at [github pages](https://brunofaria1322.github.io/Simulator) / Futurely at [readthedocs](https://readthedocs.io/en/latest/).

Check [GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/) to write this file.

---

Since we are using a src structure, we need to install the package in editable mode to be able to import it.

- `pip install -e .`

---

build:

- `py -m build`

test build:

- `twine check dist/*`

upload to pypi:

- `twine upload dist/*`

---

Pyhton version: 3.12.0

sphinx (version 7.3.7)

- pip install sphinx
- sphinx-quickstart docs
- cd docs
- make html
  - (on windows) .\make.bat html

Autobuild

- pip install sphinx-autobuild
- sphinx-autobuild docs\source\ docs\build\html

Myst

- pip install rst-to-myst[sphinx]
- rst2myst convert docs\*\*\*.rst
- delete all .rst files
- add myst_parser to extensions of conf.py
- pip install myst-parser
- do the make html again

Future:

- actions:
  - [ ] deploy to pypi
  - [ ] deploy to readthedocs
  - [x] deploy to github pages
