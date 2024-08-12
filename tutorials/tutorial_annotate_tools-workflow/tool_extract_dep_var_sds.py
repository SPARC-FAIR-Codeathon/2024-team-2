"""
Created on 11/08/2024 (NZT time)

This tool extracts the dependent variable measurements from a SDS dataset at the
corresponding independent variable measurements from tool_extract_indep_var_sds.py.

Author: Max Dang Vu
Organisation: Auckland Bioengineering Institute
"""

import argparse
import os

import numpy as np


def extract_dependent_variable_sds(xFile, outputFile):
    """
    This function extracts an array of the dependent variable measurements from a SDS dataset
    at the specified independent variable measurements from tool_extract_indep_var_sds.py.
    The dependent variable measurements are also saved to a .txt file.

    :param xFile: independent variable quantity measurements from dataset extracted from a .txt file
    :type xFile: directory
    :param outputFile: Output filename for .txt file
    :type outputFile: str
    """

    #   Get full path to script file
    dir_path = os.path.abspath('')
    outputPath = os.path.join(dir_path, 'outputs')

    #   Load file
    x = np.loadtxt(os.path.join(outputPath, xFile), delimiter=',')

    get_electrodes = False

    #   Electrodes used to measure membrane voltage in each case
    if get_electrodes:
        electrodes = ["Cuff 1", "Cuff 3", "LIFE 2"]

    #   Dependent variable quantity of dataset is membrane voltage obtained from different electrodes
    #   at the specified time measurements (x). This information was extracted from the dataset.
    y = [[-1.194679728397433872e-05,
          -1.980733829726684289e-05,
          -1.077133905927803561e-03,
          -1.519773320369282514e-04,
          4.358444211166163332e-05,
          1.658965415525065864e-05,
          2.398549602516097313e-06,
          -1.332335275220263179e-06,
          1.629816851936227506e-06,
          4.550925948376061261e-07,
          -2.440652094473894876e-07,
          -1.256780047896774447e-07,
          -1.604059700341167774e-07,
          -1.366082574509440694e-07,
          6.310354307689493841e-08,
          1.457346526672138439e-08,
          -1.628435072394222375e-07,
          -6.812635356888434155e-09,
          5.664900883157117720e-08,
          -5.565218230427167767e-09,
          2.460946088137883220e-07,
          5.694319531931366159e-08,
          -2.056334398814257176e-08,
          1.748808934360601829e-07,
          1.773989087065118717e-07,
          -1.101112467177508824e-07,
          -1.075328597482854415e-07,
          3.386144369441476939e-08,
          1.897932070755456980e-08,
          -2.771581229295496183e-08,
          -4.256350579346231629e-08,
          2.369912349741317857e-07,
          1.700902709291848032e-07,
          -1.165152584466342702e-08,
          2.526520739717943143e-08,
          7.121820226943954045e-08,
          7.056591199310062196e-09,
          -5.769651171224500800e-08,
          5.493674015745062083e-08,
          -1.013383430345409753e-07,
          9.970229271565001302e-08,
          -3.204593418913237084e-07,
          -4.325400556337169854e-07,
          -6.636738552043014031e-07,
          -9.158674234832865898e-07,
          -1.763365287119160062e-06,
          -2.739152133168838517e-06,
          -4.476083953312462761e-06,
          -7.542537164392824152e-06],
         [-8.214201655775424599e-06,
          -1.372845595816498555e-05,
          -7.999020217967099580e-04,
          -1.352363618910832938e-04,
          3.092872602419839500e-05,
          2.011895437284948941e-05,
          9.557211317360985987e-06,
          -3.820839410285373378e-06,
          -6.232610444666107165e-07,
          1.988794676647719403e-06,
          1.798649238333572180e-07,
          -6.153998549570629156e-08,
          -2.280486447432810844e-08,
          1.406398600829660458e-07,
          2.274509841389832947e-07,
          2.300306274820511094e-08,
          -1.572653510349146469e-08,
          -3.974936120421572610e-09,
          -1.433040571137541349e-07,
          -6.573999965324418493e-08,
          -2.177186888257862627e-07,
          8.583061039754071028e-08,
          3.093779432661249251e-07,
          -2.944427710333310390e-08,
          -3.330317444469355433e-08,
          -6.162516141635240061e-08,
          -1.202485970381447797e-07,
          -3.076161062497104022e-08,
          2.313064439128372287e-10,
          2.292993146737572915e-08,
          -1.411246583126800866e-07,
          -2.647507798588564735e-08,
          3.457814694547747936e-08,
          3.535925893357380257e-08,
          -3.418105614165993230e-08,
          -1.583688933718167217e-07,
          1.012797271590110401e-07,
          2.562090584582817896e-07,
          -2.444895666644071396e-08,
          -4.979131491438313074e-08,
          -2.076604778027471311e-07,
          -1.452476801605392218e-07,
          -1.909545607780813125e-07,
          -4.140272436638787089e-07,
          -5.639934119954284032e-07,
          -1.227500442716898632e-06,
          -1.947706456334992766e-06,
          -3.273951913389777314e-06,
          -5.192352644414561846e-06],
         [-1.462083138277712432e-06,
          -2.622262173064377229e-06,
          -7.534344594908582143e-04,
          4.759606952424768331e-05,
          9.223688791069610846e-06,
          1.677105825408498600e-05,
          2.933277337991895692e-06,
          8.110282750876216604e-07,
          -1.425914101175619564e-06,
          -1.663120625907863012e-06,
          -9.908095184916553125e-08,
          2.624454673115753441e-07,
          -1.624587473395667151e-07,
          3.338108641988796370e-08,
          4.483677957255745166e-08,
          -2.272849655834033843e-08,
          6.738530411162273816e-08,
          -1.318730119721173922e-07,
          2.174619084598256286e-08,
          -2.635504384574270156e-08,
          -2.126007975966536514e-07,
          -1.018217795072811392e-07,
          -1.916260472310982058e-08,
          -6.106306355050666979e-08,
          -9.495394166931023019e-09,
          -3.854787158901162777e-09,
          -1.056476775362339673e-07,
          4.154432204662217048e-08,
          5.605603793178550658e-08,
          -7.432304252075775190e-08,
          -8.398636677852381007e-08,
          -1.854658209056216439e-07,
          -8.286421105874349958e-08,
          -1.424359400919484305e-07,
          -2.010722883843532184e-07,
          7.429247114041876855e-08,
          6.948458981206337186e-08,
          -1.446947117729709508e-07,
          -5.107443403085964430e-08,
          4.225381293752249147e-10,
          6.443742709884127751e-08,
          4.906226138658068876e-08,
          -9.440736302779392982e-08,
          -2.710204727223795743e-07,
          1.652564732815241083e-09,
          -8.563504499159779379e-08,
          -4.766724708442070395e-07,
          -7.328525557563466932e-07,
          -8.203079358028723468e-07]]

    #   Save independent variable measurement to .txt files
    os.makedirs(outputPath, exist_ok=True)
    np.savetxt(os.path.join(outputPath, outputFile), np.array(y).T, delimiter=',')


def main():
    #   Set up argument parse for command line execution
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--xFile", required=True, help="")
    parser.add_argument("--outputFile", required=True, help="")
    args = parser.parse_args()

    #   Extract voltage measurements from this SDS dataset for three different channels
    #   (https://sparc.science/datasets/262?type=dataset)
    extract_dependent_variable_sds(xFile=args.xFile, outputFile=args.outputFile)


if __name__ == "__main__":
    main()
