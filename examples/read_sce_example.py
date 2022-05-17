#!/usr/bin/env python
"""Example script to read a SingleCellExperiment from scFlow

Usage:
    ./read_sce_example.py /path/to/sce_folder/

Author:
    Combiz Khozoie, Ph.D.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import scflowpy


def main(argv):
    if len(argv) == 1:
        filename = input("Enter filename: ")
    elif len(argv) == 2:
        filename = argv[1]
    else:
        raise SystemExit(f"Usage: {argv[0]} [ filename ]")

    sce = scflowpy.read_sce(filename)
    print(sce)


if __name__ == "__main__":
    import sys

    main(sys.argv)
