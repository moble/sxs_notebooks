#! /usr/bin/env python

import pathlib
import nbformat

for ipynb in pathlib.Path(".").glob("*.ipynb"):
    with ipynb.open("r") as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    nb["metadata"]["kernelspec"]["name"] = "conda-env-notebook-py"
    with ipynb.open("w") as f:
        nbformat.write(nb, f)
