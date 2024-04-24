# Simulator

Pyhton version: 3.12.0

sphinx (version 7.3.7)
- pip install sphinx
- sphinx-quickstart docs
- cd docs
- make html
    - (on windows) .\make.bat html

Myst
- pip install rst-to-myst[sphinx]
- rst2myst convert docs\**\*.rst
- delete all .rst files
- pip install myst-parser
- do the make html again

```bash
root
├── docs
│   └── ...
├── simulator
│   ├── datacenter
│   │   ├── __init__.py
│   │   ├── cpu.py
│   │   ├── datacenter.py
│   │   ├── disk.py
│   │   ├── host.py
│   │   ├── power.py
│   │   └── ram.py
│   ├── network
│   │   ├── __init__.py
│   │   └── link.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── works
│   │   ├── __init__.py
│   │   ├── task.py
│   │   └── task_generator.py
│   ├── __init__.py
│   └── simulator.py
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── setup.py
```
