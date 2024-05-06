# Simulator

<h1 align="center">Simulator</h1>
<div align="center">
  <a href="https://github.com/brunofaria1322/Simulator/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-GPL%203.0-red.svg" alt="License">
  </a>
  <a>
    <img src="https://img.shields.io/badge/python-3.12-blue.svg" alt="Python 3.12">
  </a>
</div>

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
