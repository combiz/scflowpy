"""Read a SingleCellExperiment from scFlow

A module with the main function 'read_sce' that reads a
SCE generated by the R package scFlow or the nf-core/scflow
pipeline into a AnnData object.

Author:
    Combiz Khozoie, Ph.D. <c.khozoie@imperial.ac.uk>

Created:
    22 November, 2021
"""

# imports
import os
from pathlib import Path

import pandas as pd
from anndata import read_mtx
from hamcrest import assert_that, instance_of
from rich import print
from rich.markdown import Markdown


# modules
def read_sce(folder_path):
    """Read a scFlow SingleCellExperiment from a folder into an AnnData Object
    Parameters
    ---------
    folder_path: str
        Folder path to the previously saved SingleCellExperiment from scFlow

    Returns
    ---------
    adata: AnnData
        An :class:`~anndata.AnnData` object
    """

    print(Markdown("**Reading SingleCellExperiment**"))

    # input folder checks
    assert_that(folder_path, instance_of(str))
    folder_path = Path(folder_path)
    assert_that(folder_path.is_dir(), True)

    adata = _read_sce_mtxandmeta(folder_path)
    adata = _read_sce_reduceddims(folder_path, adata)

    print("Imported SingleCellExperiment as AnnData Object")

    return adata


def _read_sce_mtxandmeta(folder_path):
    """Read the sparse matrix and metadata for a scFlow SingleCellExperiment
    from a folder into an AnnData Object

    Parameters
    ---------
    folder_path: str
        Folder path to the previously saved SingleCellExperiment from scFlow

    Returns
    ---------
    adata: AnnData
        An :class:`~anndata.AnnData` object
    """

    paths_d = {
        "all_coldata": folder_path / "sce-coldata.tsv",
        "all_rowdata": folder_path / "sce-rowdata.tsv",
        "col_classes": folder_path / "scecoldata_classes.tsv",
        "barcodes_path": folder_path / "barcodes.tsv.gz",
        "features_path": folder_path / "features.tsv.gz",
        "matrix_path": folder_path / "matrix.mtx.gz",
    }

    for fp in paths_d:
        assert_that(paths_d[fp].exists(), True)

    print("Reading sparse matrix:", paths_d["matrix_path"])
    adata = read_mtx(paths_d["matrix_path"])
    adata = adata.transpose()

    print("Reading observation data: ", paths_d["all_coldata"])
    coldata = pd.read_csv(paths_d["all_coldata"], header=0, sep="\t")
    print("Reading variable data: ", paths_d["all_rowdata"])
    rowdata = pd.read_csv(paths_d["all_rowdata"], header=0, sep="\t")

    adata.obs = coldata
    adata.obs_names = adata.obs["barcode"]
    adata.var = rowdata
    adata.var_names = adata.var["gene"]

    # convert data.frame column data type to pandas equivalent
    print("Reading column classes:", paths_d["col_classes"])
    coltypes = pd.read_csv(paths_d["col_classes"], header=None, sep="\t")
    r2py_types_map_d = {
        "factor": "category",
        "character": "category",
        "integer": "int64",
        "numeric": "float",
        "logical": "boolean",
    }

    for col in coltypes[0].values:
        old_type = coltypes.loc[coltypes[0] == col][1].values[0]
        new_type = r2py_types_map_d[old_type]
        adata.obs[col] = adata.obs[col].astype(new_type, errors="ignore")

    return adata


def _read_sce_reduceddims(folder_path, adata):
    """Read the reduced dimension embeddings for a scFlow SingleCellExperiment
    from a folder into an AnnData Object

    Parameters
    ---------
    folder_path: str
        Folder path to the previously saved SingleCellExperiment from scFlow

    adata: AnnData
        An :class:`~anndata.AnnData` object with the matrix and metadata

    Returns
    ---------
    adata: AnnData
        An :class:`~anndata.AnnData` object appended with reduced dimension
         matrices (if any)
    """

    # generate dictionary of reduced_dim_name : file_path
    rd_files = [
        folder_path / filename
        for filename in os.listdir(folder_path)
        if filename.startswith("ReducedDim_")
    ]
    rd_files_d = dict.fromkeys(rd_files)
    for filename in rd_files:
        filename_sans_ext = Path(os.path.splitext(filename)[0]).stem
        rd_files_d[filename] = str(filename_sans_ext).lstrip("ReducedDim_")

    rd_files_d = {
        value: key for (key, value) in rd_files_d.items()
    }  # set the filename_sans_ext as key

    # read files and append to AnnData object
    for rd_name in rd_files_d:
        print("Reading embedding:", rd_files_d[rd_name])
        rd_df = pd.read_csv(rd_files_d[rd_name], header=0, sep="\t")
        adata.obsm[rd_name] = rd_df.values

    return adata
