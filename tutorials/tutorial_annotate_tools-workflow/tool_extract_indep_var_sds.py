"""
Created on 11/08/2024 (NZT time)

This tool obtains a SDS dataset via its ID and obtains the
independent variable measurements from the dataset.

Author: Max Dang Vu
Organisation: Auckland Bioengineering Institute
"""

import argparse
import os

import numpy as np
from sparc_me import Dataset_Api


def extract_independent_variable_sds(datasetId, versionId, outputFile):
    """
    This function extracts an array of measurements of the independent
    variable quantity of a SDS dataset with a known Pensieve dataset ID,
    and saves the array to a .txt file.

    :param datasetId: SPARC dataset ID
    :type datasetId: float
    :param versionId: SPARC dataset version ID
    :type versionId: float
    :param outputFile: Output filename for .txt file
    :type outputFile: str
    """

    # Get dataset metadata from SPARC Portal
    api_tools = Dataset_Api()
    metadata = api_tools.get_metadata_pensieve(datasetId, versionId)

    # Note we can download the dataset from SPARC using the sparc-me API using the line below
    # api_tools.download_dataset(dataset["id"])

    # This is commented out as the dataset is >29.63 GB, we downloaded the target subject
    # data directly from the SPARC portal, processed the data and saved the outputs.

    # Independent variable quantity of dataset is time, and this was extracted from the dataset
    x = [0.000000000000000000e+00,
         8.191999999999999629e-04,
         1.638399999999999926e-03,
         2.457599999999999889e-03,
         3.276799999999999852e-03,
         4.095999999999999815e-03,
         4.915199999999999778e-03,
         5.734399999999999741e-03,
         6.553599999999999703e-03,
         7.372799999999999666e-03,
         8.191999999999999629e-03,
         9.011200000000000460e-03,
         9.830399999999999555e-03,
         1.064960000000000039e-02,
         1.146879999999999948e-02,
         1.228800000000000031e-02,
         1.310719999999999941e-02,
         1.392640000000000024e-02,
         1.474559999999999933e-02,
         1.556480000000000016e-02,
         1.638399999999999926e-02,
         1.720319999999999835e-02,
         1.802240000000000092e-02,
         1.884160000000000001e-02,
         1.966079999999999911e-02,
         2.048000000000000168e-02,
         2.129920000000000077e-02,
         2.211839999999999987e-02,
         2.293759999999999896e-02,
         2.375680000000000153e-02,
         2.457600000000000062e-02,
         2.539519999999999972e-02,
         2.621439999999999881e-02,
         2.703360000000000138e-02,
         2.785280000000000047e-02,
         2.867199999999999957e-02,
         2.949119999999999867e-02,
         3.031040000000000123e-02,
         3.112960000000000033e-02,
         3.194879999999999942e-02,
         3.276799999999999852e-02,
         3.358719999999999761e-02,
         3.440639999999999671e-02,
         3.522560000000000274e-02,
         3.604480000000000184e-02,
         3.686400000000000093e-02,
         3.768320000000000003e-02,
         3.850239999999999913e-02,
         3.932159999999999822e-02]

    #   Get full path to script file
    dir_path = os.path.abspath('')

    #   Save independent variable measurement to .txt files
    outputPath = os.path.join(dir_path, 'outputs')
    os.makedirs(outputPath, exist_ok=True)
    np.savetxt(os.path.join(outputPath, outputFile), np.array(x), delimiter=',')


def main():

    #   Set up argument parse for command line execution
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--datasetId", required=True, help="")
    parser.add_argument("--versionId", required=True, help="")
    parser.add_argument("--outputFile", required=True, help="")
    args = parser.parse_args()

    #   Extract time measurements from this SDS dataset
    #   (https://sparc.science/datasets/262?type=dataset)
    extract_independent_variable_sds(
        datasetId=args.datasetId, versionId=args.versionId, outputFile=args.outputFile)


if __name__ == "__main__":
    main()
