# SPARC Assemble (sparc-assemble)
A Python tool to find and automatically assemble tools and workflows to process SPARC datasets in accordance with FAIR principles

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/SPARC-FAIR-Codeathon/2024-team-2.svg)](https://GitHub.com/SPARC-FAIR-Codeathon/2024-team-2/issues?q=is%3Aissue+is%3Aclosed)
[![Issues][issues-shield]][issues-url]
[![apache License][license-shield]][license-url]
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)
<!--* [![DOI](https://zenodo.org/badge/XXXX.svg)](https://zenodo.org/badge/latestdoi/XXXXX) -->
[![PyPI version fury.io](https://badge.fury.io/py/sparc-assemble.svg)](https://pypi.python.org/pypi/sparc-assemble/)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/2024-team-2.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-2/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/2024-team-2.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-2/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/2024-team-2.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-2/issues
[license-shield]: https://img.shields.io/github/license/SPARC-FAIR-Codeathon/2024-team-2.svg?style=flat-square
[license-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/LICENSE
[lines-of-code-shield]: https://img.shields.io/tokei/lines/github/SPARC-FAIR-Codeathon/2024-team-2
[lines-of-code-url]: #

## Table of contents
* [About](#about)
* [Introduction](#introduction)
* [The problem](#the-problem)
* [Our solution - sparc-assemble](#our-solution---sparc-assemble)
* [Impact and vision](#impact-and-vision)
* [Future developments](#future-developments)
* [Setting up sparc-assemble](#setting-up-sparc-assemble)
* [Using sparc-assemble](#using-sparc-assemble)
* [Reporting issues](#reporting-issues)
* [Contributing](#contributing)
* [Cite us](#cite-us)
* [FAIR practices](#fair-practices)
* [License](#license)
* [Team](#team)
* [Acknowledgements](#acknowledgements)

## About
This is the repository of Team sparc-assemble (Team #2) of the 2024 SPARC Codeathon. Click [here](https://sparc.science/help/2024-sparc-fair-codeathon) to find out more about the SPARC Codeathon 2024. Check out the [Team Section](#team) of this page to find out more about our team members.

Please see the [Acknowledgements](#acknowledgements) section of this readme for a list of tools that have been used in this project.

## Introduction
The NIH Common Fund program on **[Stimulating Peripheral Activity to Relieve Conditions (SPARC)](https://commonfund.nih.gov/sparc) focuses on understanding peripheral nerves** (nerves that connect the brain and spinal cord to the rest of the body), **how their electrical signals control internal organ function**, and **how therapeutic devices could be developed to modulate electrical activity in nerves to improve organ function**. This may provide a potentially powerful way to treat a diverse set of common conditions and diseases such hypertension, heart failure, gastrointestinal disorders, and more. 60 research groups spanning 90 institutions and companies contribute to SPARC and work across over 15 organs and systems in 8 species.

**The [SPARC Portal](http://sparc.science/) provides a single user-facing online interface to resources** that can be shared, cited, visualized, computed, and used for virtual experimentation. A **key offering** of the portal is the **collection of well-curated datasets in a standardised format, including anatomical and computational models** that are being generated both SPARC-funded researchers and the international scientific community. These datasets can be found under the "[Find Data](https://sparc.science/data?type=dataset)" section of the SPARC Portal. Information regarding [how to navigate a SPARC dataset](https://docs.sparc.science/docs/navigating-a-sparc-dataset) and [how a dataset is formatted](https://docs.sparc.science/docs/overview-of-sparc-dataset-format) can be found on the SPARC Portal.

**The scientific community is developing tools to process the original data and generate new results, outcomes, and knowledge**

**Workflows can be developed that apply tools** (e.g. segmentation of images, or running of computational physiology simulations) in a series of steps **to . These results (derived data) can be stored in a new standardised dataset and potentially be [contributed to the SPARC Portal](https://docs.sparc.science/docs/submitting-a-dataset-to-sparc) to support further scientific advances.

## The problem
There is **currently no option for users to**:
- **easily find and access existing tools and workflows developed by the SPARC community for processing SPARC data** 
- **easily find and access external tools that could be used for processing SPARC data**
- **easily reuse these tools to assemble and run new workflows** for:
  - processing existing SPARC data
  - helping identify new data that could be collected to fill in gaps in our knowledge
- **easily run such workflows locally or from cloud computing platforms such as oSPARC**
- **easily reproduce workflow results**
- 
## Our solution - sparc-assemble
To address this problem, we have **developed a Python module called the SPARC Assemble (sparc-assemble)** that can be used to find and automatically assemble workflows and tools to process SPARC datasets in accordance with FAIR principles:
- Provides an easy-to-use python-based application programming interface (API) to enable searching of available **tools** and **workflows**


**If you find sparc-assemble useful, please add a GitHub Star to support developments!**

### Designed to enable FAIRness

## Impact and vision
  
## Future developments
- Workflow and tool registry in SPARC portal 

## Setting up sparc-assemble

### Pre-requisites 
- [Git](https://git-scm.com/)
- Python. Tested on:
   - 3.10
- Operating system. Tested on:
  - Ubuntu 18
   
### PyPI

Here is the [link](https://pypi.org/project/sparc-assemble/) to our project on PyPI
```
pip install sparc-assemble
```

### From source code

#### Downloading source code
Clone the sparc-assemble repository from github, e.g.:
```
git clone https://github.com/SPARC-FAIR-Codeathon/2024-team-2.git
```

#### Installing dependencies

1. Setting up a virtual environment (optional but recommended). 
   In this step, we will create a virtual environment in a new folder named **venv**, 
   and activate the virtual environment.
   
   * Linux
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   * Windows
   ```
   python3 -m venv venv
   venv\Scripts\activate
   ```
   
2. Installing dependencies via pip
    ```
    pip install -r requirements.txt
    ```

## Using sparc-assemble

### Running tutorials

Guided Jupyter Notebook tutorials have been developed describing how to use sparc-assemble in different scenarios:

<table>
<thead>
  <tr>
    <th> Tutorial</th>
    <th> Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/tutorials/tutorial_1/XXX.ipynb">
    1
    </a></td>
    <td> INSERT </td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/tutorials/tutorial_2/XXX.ipynb">
    2
    </a></td>
    <td> Use sparc-assemble to ... </td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/tutorials/tutorial_3/XXX.ipynb">
    3
    </a></td>
    <td> Use sparc-assemble to run ...</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/tutorials/tutorial_4/XXX.ipynb">
    4
    </a></td>
    <td> Use sparc-assemble to run ...</td>
  </tr> 
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/tutorials/tutorial_5/XXX.ipynb">
    5
    </a></td>
    <td> Use sparc-assemble to run ...</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/tutorials/tutorial_6/XXX.ipynb">
    6
    </a></td>
    <td> Use sparc-assemble to run ...</td>
  </tr>   
</tbody>
</table>
<p align="center">
</p>
<br/>

## Reporting issues 
To report an issue or suggest a new feature, please use the [issues page](https://github.com/SPARC-FAIR-Codeathon/2024-team-2/issues). Issue templates are provided to allow users to report bugs, and documentation or feature requests. Please check existing issues before submitting a new one.

## Contributing
Fork this repository and submit a pull request to contribute. Before doing so, please read our [Code of Conduct](https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/CODE_OF_CONDUCT.md) and [Contributing Guidelines](https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/master/CONTRIBUTING.md). Pull request templates are provided to help guide developers in describing their contribution, mentioning the issues related to the pull request and describing their testing environment. 

### Project structure
* `/sparc_assemble/` - Parent directory of sparc-assemble python module.
* `/sparc_assemble/core/` - Core classes of sparc-assemble.
* `/resources/` - Resources that are used in tutorials (e.g. SDS datasets containing workflow and tool descriptions).
* `/tutorials/` - Parent directory of tutorials for using sparc-assemble.
* `/development_examples/` - Parent directory of examples that were created during the development of sparc-assemble.
* `/docs/images/` - Images used in sparc-assemble tutorials.

## Cite us
If you use sparc-assemble to make new discoveries or use the source code, please cite us as follows:
```
Mathilde Verlyck, Jiali Xu, Max Dang Vu, Thiranja Prasad Babarenda Gamage, Chinchien Lin (2024). sparc-assemble: v1.0.0 - A Python tool to find and automatically assemble tools and workflows to process SPARC datasets in accordance with FAIR principles. Zenodo. https://doi.org/XXXX/zenodo.XXXX.
```

## FAIR practices
We have assessed the FAIRness of our sparc-assemble tool against the FAIR Principles established for research software. The details are available in the following [document](https://docs.google.com/document/d/1az_LXPivQvaofTsiMktJaWpyy2W_xKGX/edit).

## License
sparc-assemble is fully open source and distributed under the very permissive Apache License 2.0. See [LICENSE](https://github.com/SPARC-FAIR-Codeathon/2024-team-2/blob/main/LICENSE) for more information.

## Team
* Mathilde Verlyck <mver587@aucklanduni.ac.nz> (Developer, Writer - Documentation)
* [Jiali Xu](https://github.com/JialiXu12) (Developer, Writer - Documentation)
* Max Dang Vu <mdan066@aucklanduni.ac.nz>  (Developer, Writer - Documentation)
* [Thiranja Prasad Babarenda Gamage](https://github.com/PrasadBabarendaGamage) (Writer - Documentation)
* [Chinchien Lin](https://github.com/LIN810116) (Lead, SysAdmin)

## Acknowledgements
- We would like to thank the organizers of the 2024 SPARC Codeathon for their guidance and support during this Codeathon.
