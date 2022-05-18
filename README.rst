========
scflowpy
========

.. image:: https://img.shields.io/pypi/v/scflowpy.svg
        :target: https://pypi.python.org/pypi/scflowpy

.. image:: https://github.com/combiz/scflowpy/workflows/CI/badge.svg?branch=main
     :target: https://github.com/combiz/scflowpy/actions?workflow=CI
     :alt: CI Status

.. image:: https://readthedocs.org/projects/scflowpy/badge/?version=latest
        :target: https://scflowpy.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

scFlowPy is a helper package to bridge scFlow with the Python ecosystem.
A typical use case is to allow tertiary scRNAseq analyses on scFlow outputs
using Python tools (e.g. Tensorflow, PyTorch, Scanpy, `and others <https://github.com/seandavi/awesome-single-cell>`_).

The core function currently is provided by ``read_sce()``, allowing users to read any SingleCellExperiment object
output by scFlow (or by the nf-core/scflow pipeline) into the Annotated data
(`AnnData <https://anndata.readthedocs.io/en/latest/>`_) format.


* Free software: GNU General Public License v3
* Documentation: https://scflowpy.readthedocs.io.

Credit
________

Written by Dr Combiz Khozoie for The Department of Brain Sciences, Imperial College London.
