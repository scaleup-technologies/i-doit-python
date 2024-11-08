#!/bin/bash

# See also: https://packaging.python.org/en/latest/tutorials/packaging-projects/
if [ ! -f ~/.pypirc ] ; then
   echo Please create a ~/.pypirc file first, see:
   echo https://packaging.python.org/en/latest/specifications/pypirc/
   exit 1
fi
rm -rf dist
.venv/bin/python3 -m build
.venv/bin/twine upload --repository pypi dist/*

# FIXME Add gitlab tagging
echo Install:
echo python3 -m pip install  idoit_scaleup
