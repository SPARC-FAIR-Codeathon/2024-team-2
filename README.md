# SPARC Assemble (sparc-assemble)
A Python tool to automatically assemble models and tools into workflows to process SPARC datasets in accordance with FAIR principles.

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
* [Vision](#vision)
* [Benefits](#benefits)
* [Our solution - sparc-assemble](#our-solution---sparc-assemble)
* [Designed to enable FAIRness](#designed-to-enable-fairness)
* [Future developments](#future-developments)
* [Setting up sparc-assemble](#setting-up-sparc-assemble)
* [Using sparc-assemble](#using-sparc-assemble)
* [Reporting issues](#reporting-issues)
* [Contributing](#contributing)
* [Cite us](#cite-us)
* [License](#license)
* [Team](#team)
* [Acknowledgements](#acknowledgements)

## About
This is the repository of Team sparc-assemble (Team #2) of the 2024 SPARC Codeathon. Click [here](https://sparc.science/help/2024-sparc-fair-codeathon) to find out more about the SPARC Codeathon 2024. Check out the [Team Section](#team) of this page to find out more about our team members.

Please see the [Acknowledgements](#acknowledgements) section of this readme for a list of tools that have been used in this project.

## Introduction
The NIH Common Fund program on **[Stimulating Peripheral Activity to Relieve Conditions (SPARC)](https://commonfund.nih.gov/sparc) focuses on understanding peripheral nerves** (nerves that connect the brain and spinal cord to the rest of the body), **how their electrical signals control internal organ function**, and **how therapeutic devices could be developed to modulate electrical activity in nerves to improve organ function**. This may provide a potentially powerful way to treat a diverse set of common conditions and diseases such hypertension, heart failure, gastrointestinal disorders, and more. 60 research groups spanning 90 institutions and companies contribute to SPARC and work across over 15 organs and systems in 8 species.

**The [SPARC Portal](http://sparc.science/) provides a single user-facing online interface to resources** that can be shared, cited, visualized, computed, and used for virtual experimentation. A **key offering** of the portal is the **collection of well-curated datasets in a standardised format, including anatomical and computational models** that are being generated both SPARC-funded researchers and the international scientific community. These datasets can be found under the "[Find Data](https://sparc.science/data?type=dataset)" section of the SPARC Portal. Information regarding [how to navigate a SPARC dataset](https://docs.sparc.science/docs/navigating-a-sparc-dataset) and [how a dataset is formatted](https://docs.sparc.science/docs/overview-of-sparc-dataset-format) can be found on the SPARC Portal.

**The scientific community is developing new tools and models** to process and understand measurements in these datasets to generate new results, outcomes, and knowledge. These tools and models are often applied in a series of steps to create workflows whose outputs provide quantities of interest. For example, a user may be creating a workflow that inputs medical images of the brain (measurement) and segments brain tissue from these images (tool) that can output brain volume (quantity of interest). Another user maybe interest in a workflow that inputs electrode measurements from the surface of the heart to personalise a computational model of cardiac electrophysiology to quantify activation patterns. These workflows may require multiple intermediate tools and models to generate the final output of interest. 

In addition to Significant effort has been made globally to make 

## The problem
Despite users having an general idea of the quantities of interest in their investigations (e.g. outputs of specific models or tools they are developing), they typically need to assemble workflows manually, often guessing what inputs and intermediate measurements, models, and tools may be needed.
There is **currently no option for users to**:
- **easily find and access existing models and tools**:
  - developed by the SPARC community for processing SPARC data 
  - developed externally that could be used for processing SPARC data
- **easily assemble new workflows that reuse existing models and tools to evaluate quantities of interest**
- **easily identify which measurements (e.g. SPARC datasets) already contain the necessary inputs for these new workflows**
- **easily identify which measurements, tools, and/or models may be missing** to support effcient advancement of research efforts 

## Vision
- Provide capability to automatically assemble workflows by integrating existing measurements models, tools of interest X of interest
- Link with Language Models to support
- Run these newly created workflows locally or in existing platforms such as oSPARC. 
- These results (derived data) can be stored in a new standardised dataset and potentially be [contributed to the SPARC Portal](https://docs.sparc.science/docs/submitting-a-dataset-to-sparc) to support further scientific advances.

## Benefits
- This would provide substantial improvemtns to enrich
- Maximise finability and impact of existing SPARC resoures
- Support priorite new investigations for gathering new knowledge (e.g. collecting new data or developing new models or tools)
- Support efforts for FAIR 
- help identify which measurements  models, tools  avenues for research to fill in gaps in our knowledge and capabilities

## Our solution - sparc-assemble
To address this problem and support the vision, we have **developed a Python module called SPARC Assemble (sparc-assemble)** that can be used to find, access, and automatically assemble models and tools into workflows to process SPARC datasets in accordance with FAIR principles with the following features: 
- Extract and annotate existing tools and models from SPARC datasets
- Access existing tools and models from external repositories such as [WorkflowHub](https://workflowhub.eu) and Biomodels
- Store information about the model and tools in a local knowledge graph defined by the standardised [EDAM ontology](http://edamontology.org) (which has been deveoped for bioscientific data analysis and data management)
- List all available models and tools
- Perform queries to automatically assemble workflows:
  - List all possible workflows (model and tool combinations) that would enable evaluation of a quantity of interest (ie an output of a model or tool)
  - Identify which SPARC datasets contain the required inputs to the workflow
  - Idenitfy which measurement, model, and tool inputs are missing
- Provides a natural language inteface to  
- Provides an easy-to-use python-based application programming interface (API) to provide the above functionality 
- Provides a series of tutorials
  
## Designed to enable FAIRness
We have assessed the FAIRness of our sparc-assemble tool against the FAIR Principles established for research software. The details are available in the following [document](INSERT GOOGLE DOC).

## Future developments
- Workflow and tool registry in SPARC portal
- Improve how the knowledge graph Include persistent identifiers in the knowledge graph
- Expand tool descriptions that can be access e.g. Workflow Description Language, Nextflow, Snakemake etc 

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

**If you find sparc-assemble useful, please add a GitHub Star to support developments!**

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
