# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Simulator"
copyright = "2024, Bruno Faria"
author = "Bruno Faria"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # Markdown support
    "sphinx.ext.duration",  # Duration of deployment
    "sphinx.ext.autosectionlabel",  # Auto section labels
    "sphinx.ext.autodoc",  # Automatic documentation
    "sphinx.ext.napoleon",  # NumPy and Google style docstrings
    "nbsphinx",  # Jupyter notebook support
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
