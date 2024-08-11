"""
Created on 11/08/2024 (NZST time)

This tool converts extracted data from the SDS dataset of a study
and displays key results of the study.

Author: Max Dang Vu
Organisation: Auckland Bioengineering Institute
"""

import argparse
import json
import os

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.size"] = 18


def display_output(input_json, file_type):
    """
    This function displays plots of key results from the study

    :param input_json: path to json file containing study data files
    :type input_json: string
    :param file_type: type of file saved
    :type file_type: string
    :return: plot of study results saved as .png file
    :rtype: str
    """
    #   Access file paths to measurements
    output_files = json.load(open(input_json))

    #   Load key measurements and info (time, voltage, electrode name)
    time = np.loadtxt(output_files['data']['time'])
    voltage = np.loadtxt(output_files['data']['voltage'])
    with open(output_files['equipment']['electrodes']) as f:
        electrodes = [line for line in f]

    #   Plot the key results
    fig, ax = plt.subplots(figsize=(15, 9))
    for i in range(voltage.shape[1]):  # add desired channels to plot here
        plt.plot(time * 1e3, voltage[:, i] * 1e6, label=str(electrodes[2 * i]))

    plt.xlabel('Time (ms)')
    plt.ylabel(r'Voltage ($\mu$V)')
    plt.xlim([1, 9])  # 1-9 for Abeta, 1-19 for B
    plt.ylim([-150, 150])  # 150 for Abeta, 20 for B
    plt.legend(loc='upper right', fontsize=14)
    plt.xlabel('Time (ms)', fontsize=14)
    plt.ylabel('Voltage (uV)', fontsize=14)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Example dataset 1")
    plt.savefig(os.path.join(f'outputs', f'summary_result{file_type}'))
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--input_json", required=True, help="")
    parser.add_argument("--file_type", required=True, help="")
    args = parser.parse_args()

    display_output(input_json=args.input_json, file_type=args.file_type)


if __name__ == "__main__":
    main()
