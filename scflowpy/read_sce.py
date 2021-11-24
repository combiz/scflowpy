"""Read a SingleCellExperiment from scFlow
A module with the main function 'read_sce' that imports a
SCE generated with the R package scFlow from a folder

Author: Combiz Khozoie, Ph.D. <c.khozoie@imperial.ac.uk>
Created: 22 November, 2021
"""
# imports
import os
from hamcrest import *                  # for validation checks
from pathlib import Path                # for file path validation
from rich import print                  # for rich terminal text
from rich.markdown import Markdown      # for rich terminal text
import pandas as pd                     # to handle tsv files
from anndata import AnnData, read_mtx   # for generating the AnnData object


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

    print(Markdown("# Reading SingleCellExperiment"))

    # input folder checks
    assert_that(folder_path, instance_of(str))
    folder_path = Path(folder_path)
    assert_that(folder_path.is_dir(), True)

    paths_d = {
        'all_coldata': folder_path / 'sce-coldata.tsv',
        'all_rowdata': folder_path / 'sce-rowdata.tsv',
        'col_classes': folder_path / 'scecoldata_classes.tsv',
        'barcodes_path': folder_path / 'barcodes.tsv.gz',
        'features_path': folder_path / 'features.tsv.gz',
        'matrix_path': folder_path / 'matrix.mtx.gz'
    }

    for fp in paths_d:
        assert_that(paths_d[fp].exists(), True)

    print("Reading sparse matrix:", paths_d['matrix_path'])
    adata = read_mtx(paths_d['matrix_path'])
    adata = adata.transpose()

    print("Reading observation data: ", paths_d['all_coldata'])
    coldata = pd.read_csv(paths_d['all_coldata'], header=0, sep='\t')
    print("Reading variable data: ", paths_d['all_rowdata'])
    rowdata = pd.read_csv(paths_d['all_rowdata'], header=0, sep='\t')

    adata.obs = coldata
    adata.obs_names = adata.obs["barcode"]
    adata.var = rowdata
    adata.var_names = adata.var["gene"]

    # generate dictionary of reduced_dim_name : file_path
    rd_files = [folder_path / filename for filename in os.listdir(folder_path) if filename.startswith("ReducedDim_")]
    rd_files_d = dict.fromkeys(rd_files)
    for filename in rd_files:
        filename_sans_ext = Path(os.path.splitext(filename)[0]).stem
        rd_files_d[filename] = str(filename_sans_ext).lstrip("ReducedDim_")

    rd_files_d = {value: key for (key, value) in rd_files_d.items()} # set the filename_sans_ext as key

    # read files and append to AnnData object
    for rd_name in rd_files_d:
        print("Reading embedding:", rd_files_d[rd_name])
        rd_df = pd.read_csv(rd_files_d[rd_name], header=0, sep='\t')
        adata.obsm[rd_name] = rd_df.values

    #coltypes = pd.read_csv("/home/ckhozoie/Documents/junk/final_sce/scecoldata_classes.tsv", header=0, sep='\t')
    #r2py_types_map_d = {
    #    'factor': 'category',
    #    'character': 'category',
    #    'integer': 'int64',
    #    'numeric': 'float'
    #}

    #for col in ['parks', 'playgrounds', 'sports', 'roading']:
    #    public[col] = public[col].astype('category')

    print("Imported SingleCellExperiment as AnnData Object")

    return adata
