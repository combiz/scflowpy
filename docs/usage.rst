=====
Usage
=====

To use scflowpy to generate an :py:class:`anndata.AnnData` object from a SingleCellExperiment object previously output by scFlow/nf-core-scflow::

    import scflowpy
    adata = read_sce('/full/path_to/sce')
