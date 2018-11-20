#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import subprocess

import sphinx_nameko_theme

# Mock most of the dependencies
import sys
from unittest.mock import MagicMock


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = [
    "numpy",
    "astropy",
    "astropy.units",
    "astropy.constants",
    "pymc3",
    "pymc3.step_methods.hmc",
    "pymc3.distributions",
    "pymc3.distributions.transforms",
    "theano",
    "theano.ifelse",
    "theano.tensor",
]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

import exoplanet  # NOQA

# Convert the tutorials
for fn in glob.glob("_static/notebooks/*.ipynb"):
    name = os.path.splitext(os.path.split(fn)[1])[0]
    print("Building {0}...".format(name))
    subprocess.check_call(
        "jupyter nbconvert --template tutorials/tutorial_rst --to rst "
        + fn + " --output-dir tutorials", shell=True)

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'astropy': ('http://docs.astropy.org/en/stable/', None),
}

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

# General information about the project.
project = "exoplanet"
author = "Dan Foreman-Mackey"
copyright = "2018, " + author

version = exoplanet.__version__
release = exoplanet.__version__

exclude_patterns = ["_build"]
pygments_style = "sphinx"

# Readthedocs.
# on_rtd = os.environ.get("READTHEDOCS", None) == "True"
html_theme_path = [sphinx_nameko_theme.get_html_theme_path()]
html_theme = "nameko"

html_context = dict(
    display_github=True,
    github_user="dfm",
    github_repo="exoplanet",
    github_version="master",
    conf_py_path="/docs/",
)
html_static_path = ["_static"]
html_show_sourcelink = False
