# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'dva-52'
copyright = '2025, Johannes Geiger, Dennis Gruener, Elias Haggenmueller, Seyit Kaya, Moritz Kramer'
author = 'Johannes Geiger, Dennis Gruener, Elias Haggenmueller, Seyit Kaya, Moritz Kramer'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
import glob

# Füge src zum Python-Pfad hinzu
sys.path.insert(0, os.path.abspath('../../src'))

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
