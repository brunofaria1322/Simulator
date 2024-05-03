# Simulator

Check [GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/) to write this file.

---
build:
- `py -m build`

test build:
- `twine check dist/*`

upload to test:
- `twine upload -r testpypi dist/*`

install from test:
- `pip install -i https://test.pypi.org/simple/ simulator`

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
