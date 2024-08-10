# SPARC Flow (sparc-assemble)
A Python tool to describe and run tools and workflows for processing SPARC datasets in accordance with FAIR principles.

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/SPARC-FAIR-Codeathon/2024-team-3.svg)](https://GitHub.com/SPARC-FAIR-Codeathon/2024-team-3/issues?q=is%3Aissue+is%3Aclosed)
[![Issues][issues-shield]][issues-url]
[![apache License][license-shield]][license-url]
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)
<!--* [![DOI](https://zenodo.org/badge/XXXX.svg)](https://zenodo.org/badge/latestdoi/XXXXX) -->
[![PyPI version fury.io](https://badge.fury.io/py/sparc-assemble.svg)](https://pypi.python.org/pypi/sparc-assemble/)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/2024-team-3.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-3/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/2024-team-3.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-3/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/2024-team-3.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-3/issues
[license-shield]: https://img.shields.io/github/license/SPARC-FAIR-Codeathon/2024-team-3.svg?style=flat-square
[license-url]: https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/LICENSE
[lines-of-code-shield]: https://img.shields.io/tokei/lines/github/SPARC-FAIR-Codeathon/2024-team-3
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
This is the repository of Team sparc-assemble (Team #3) of the 2024 SPARC Codeathon. Click [here](https://sparc.science/help/2024-sparc-fair-codeathon) to find out more about the SPARC Codeathon 2024. Check out the [Team Section](#team) of this page to find out more about our team members.

No work was done on this project prior to the Codeathon.

## Introduction
The NIH Common Fund program on **[Stimulating Peripheral Activity to Relieve Conditions (SPARC)](https://commonfund.nih.gov/sparc) focuses on understanding peripheral nerves** (nerves that connect the brain and spinal cord to the rest of the body), **how their electrical signals control internal organ function**, and **how therapeutic devices could be developed to modulate electrical activity in nerves to improve organ function**. This may provide a potentially powerful way to treat a diverse set of common conditions and diseases such hypertension, heart failure, gastrointestinal disorders, and more. 60 research groups spanning 90 institutions and companies contribute to SPARC and work across over 15 organs and systems in 8 species.

**The [SPARC Portal](http://sparc.science/) provides a single user-facing online interface to resources** that can be shared, cited, visualized, computed, and used for virtual experimentation. A **key offering** of the portal is the **collection of well-curated datasets in a standardised format, including anatomical and computational models** that are being generated both SPARC-funded researchers and the international scientific community. These datasets can be found under the "[Find Data](https://sparc.science/data?type=dataset)" section of the SPARC Portal. Information regarding [how to navigate a SPARC dataset](https://docs.sparc.science/docs/navigating-a-sparc-dataset) and [how a dataset is formatted](https://docs.sparc.science/docs/overview-of-sparc-dataset-format) can be found on the SPARC Portal.

**Workflows can be developed that apply tools** (e.g. segmentation of images, or running of computational physiology simulations) in a series of steps **to process the original data and generate new results, outcomes, and knowledge**. These results (derived data) can be stored in a new standardised dataset and potentially be [contributed to the SPARC Portal](https://docs.sparc.science/docs/submitting-a-dataset-to-sparc) to support further scientific advances.

## The problem
There is **currently no option for users to**:
- **easily describe workflows and tools, which process SPARC data, in a FAIR manner**
- **easily run such workflows locally or from cloud computing platforms such as oSPARC**
- **easily reproduce workflow results**
- **reuse tools developed for processing SPARC data in new workflows** (tools are currently bundled within and tailored to specific SPARC datasets).

## Our solution - sparc-assemble
To address this problem, we have **developed a Python module called the SPARC Flow (sparc-assemble)** that can be used to describe tools and workflows for processing SPARC datasets in accordance with FAIR principles:
- Provides an easy-to-use python-based application programming interface (API) to enable **tools** and **workflows** to be **described in a language agnostic manner**.
- Enables the parameters used for running workflows to be stored with the standardised workflow description along with a copy of its associated tools to **enable workflow results to be easily reproduced**.
- Enables **workflows and tool descriptions** to be **independently stored in SDS datasets**, **ready to be contributed to the SPARC portal** to enable reuse by others.
- Provides the ability to **save and load workflows and tools directly from/to SDS datasets** via [sparc-me](https://github.com/SPARC-FAIR-Codeathon/sparc-me).
- Provides the ability to **run workflows**:
  - locally;
  - on existing cloud computing platforms such as [oSPARC](https://osparc.io/); or
  - help prepare the workflow to be submitted to Dockstore to enable using its [standardised workflow interfaces](https://docs.dockstore.org/en/stable/advanced-topics/wes/cli-wes-tutorial.html) to run them directly from the commandline or through existing cloud computing platforms from [Dockstore.org](https://dockstore.org) (currently supports running on [AnVIL](https://anvilproject.org), [Cavatica](https://www.cavatica.org), [CGC](https://www.cancergenomicscloud.org), [DNAnexus](https://www.dnanexus.com), [Galaxy](https://usegalaxy.org), [Nextflow Tower](https://seqera.io/tower), and [Terra](https://terra.bio)).
- Provides **tutorials** that demonstrate each of the above features.
- **[Proposes guidelines for FAIR-use of tools and workflows](https://docs.google.com/document/d/1tBzDEivbl_jgdMZX6E-NYFH4vE3dlnwv/edit)**
- **Provides best practices guidance in tutorials** on how to use these guidelines.

**If you find sparc-assemble useful, please add a GitHub Star to support developments!**

### Designed to enable FAIRness
The sparc-assemble API has been designed to be agnostic to the language used to describe tools & workflows and the services it adopts to run the workflows. The following languages and services are currently supported:
- The Common Workflow Language (CWL) - is an open standard and specification used in the field of bioinformatics and scientific computing to describe and execute workflows. CWL provides a way to define and share complex computational tasks and data processing pipelines in a portable and platform-independent manner. It uses a JSON-based format to describe input data, processing steps, and output data, allowing researchers to collaborate and share reproducible analyses across different computing environments. CWL aims to enhance the ease of defining, sharing, and executing computational workflows, particularly in the context of data-intensive scientific research.
- Dockstore - is an open platform used for sharing, publishing, and discovering bioinformatics tools and workflows. It allows researchers and scientists to easily find, collaborate on, and reproduce analyses involving complex data processing pipelines. Dockstore provides a standardized way to describe and share tools and workflows using CWL and Workflow Description Language (WDL). It facilitates reproducibility in bioinformatics research by enabling users to access and execute these tools and workflows in various computational environments, such as cloud platforms, containers (e.g. Docker), or local clusters. Dockstore is Supported by [58 organisations](https://dockstore.org/organizations) including the [Global Alliance for Genomics and Health (GA4GH)](https://ga4gh.org/), the [Broad Institute](https://www.broadinstitute.org), the [Human Cell Atlas](https://humancellatlas.org/), the [Human BioMolecular Atlas Program (HuBMAP)](https://commonfund.nih.gov/hubmap), [NIH Cloud Platform Interoperability Effort](https://anvilproject.org/ncpi), the [Imaging Data Commons](https://imaging.datacommons.cancer.gov/), and [Biosimulators](https://biosimulators.org/).

We have compared FAIR-use guidelines for data and research software, and based on the literature, **[we have proposed guidelines for enabling FAIR workflows](https://docs.google.com/document/d/1tBzDEivbl_jgdMZX6E-NYFH4vE3dlnwv/edit)**. Furthermore, we have also **[provided examples of how the technologies used in sparc-assemble apply these guidelines](https://docs.google.com/document/d/1tBzDEivbl_jgdMZX6E-NYFH4vE3dlnwv/edit)**.

## Impact and vision
sparc-assemble will elevate the impact of the SPARC program by providing the fundamental tools needed by users to describe the tools and workflows they are building/using with SPARC data for generating novel results, outcomes, and knowledge. The breadth of impact spans across:
- **Supporting [SPARC Data and Resource Centre (DRC)](https://docs.sparc.science/docs/getting-started) and communnity developments** including:
  - sparc-assemble automatcially generates SDS datasets for workflows and tools that could be submitted to a "worfklow" and "tool" section of the SPARC portal's "Find data and models" page.
  - Improving efficiency of software developments (e.g. future codeathons and [SPARC portal roadmap developments](https://docs.sparc.science/docs/sparc-portal-roadmap)) by reducing the need to reimplement common functions. 
- **Supporting and promoting harmonisation/interoperability with other research initiatives**. For example, sparc-assemble enables running workflows on different platforms including those being developed in other NIH-funded initiatives such as the Common Fund’s [NIH Data Commons program](https://commonfund.nih.gov/commons). This contributes to the developers **vision for enabling workflows and to be described in a platform-agnostic manner to increase the accessibility to services provided by these platforms**. For example, users could send and run their workflows and tools to platforms that:
  - restrict access to datasets to specific territories to adhere to data-sovereignty requirements.
  - have large-scale HPC facilities that are not available in their country.
- **Supporting reuse of tools** created by users for developing novel workflows without expending limited resources in re-inventing the wheel.

Ultimately, **our vision is to include standardised workflow and tool descriptions in knowledge bases to support automated assembly and execution of workflows** (e.g. for [creating digital tiwns for precision medicine applications](https://doi.org/10.52843/cassyni.6d6bvf)).
  
## Future developments
- Automate generate of API documentation.
- support for WDL, Nextflow, and Galaxy workflow languages that are used in scientific research platforms.
- integrating workflow and tool validators and [checkers](https://docs.dockstore.org/en/stable/advanced-topics/checker-workflows.html).
- integrating workflow and tool descriptions into knowledge graphs such as [SCKAN](https://docs.sparc.science/docs/accessing-the-sparc-connectivity-knowledge-base-of-the-autonomic-nervous-system-sckan) to support the identification of workflow and tools that are related to specific biological concepts. 
- incorporating approaches for automatically assessing adherence to FAIR-ness guidelines for workflows and tools.
- tagging workflows using e.g., [Software Ontology (SWO)](https://github.com/allysonlister/swo) descriptions, that will make it easy to identify and search for workflows with e.g. [specific license restrictions](https://github.com/allysonlister/swo/blob/master/LicenceHierarchy.md).

## Setting up sparc-assemble

### Pre-requisites 
- [Git](https://git-scm.com/)
- Python. Tested on:
   - 3.9
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
git clone https://github.com/SPARC-FAIR-Codeathon/2024-team-3.git
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
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/tutorials/tutorial_1/tutorial_1_download_data_and_postprocess.ipynb">
    1
    </a></td>
    <td> Provides a typical data processing example that downloads an existing curated SDS dataset from the SPARC portal (<a href="https://doi.org/10.26275/vm1h-k4kq">Electrode design characterization for electrophysiology from swine peripheral nervous system</a>) using <a href="https://github.com/SPARC-FAIR-Codeathon/sparc-me">sparc-me</a> and perform post-processing to generate a new derived SDS dataset. This example will be used in subsequent tutorials</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/tutorials/tutorial_2/tutorial_2_creating_standarised_workflow_description.ipynb">
    2
    </a></td>
    <td> Use sparc-assemble to programmatically describe the example in Tutorial 1 in a standard workflow language (Common Workflow Language). This tutorial incorporates <a href="https://docs.google.com/document/d/1PKpl4WZ171C7YlQtG4AQ0WuK1bIFDGD6ys9PCnap_xI/edit">best practice guidelines</a> to ensure tools used in the workflow and the workflow itself are FAIR.
    </td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/tutorials/tutorial_3/tutorial_3_running_locally_with_cwltool.ipynb">
    3
    </a></td>
    <td> Use sparc-assemble to run the standardised workflow described in Tutorial 2 locally using cwltool (reference implementation provided by the CWL Organisation).</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/tutorials/tutorial_4/tutorial_4_running_locally_with_docstore.ipynb">
    4
    </a></td>
    <td> Use sparc-assemble to run the standardised workflow described in Tutorial 2 locally using Dockstore.</td>
  </tr> 
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/tutorials/tutorial_5/tutorial_5_running_on_dockstore_compatiable_cloud.ipynb">
    5
    </a></td>
    <td> Use sparc-assemble to run the standardised workflow described in Tutorial 2 via the cloud using a Dockstore-compatible cloud computing platform (e.g.  AnVIL, Cavatica, CGC, DNAnexus, Galaxy, Nextflow Tower, and Terra).</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/tutorials/tutorial_6/tutorial_6_osparc.ipynb">
    6
    </a></td>
    <td> Use sparc-assemble to run the standardised workflow described in Tutorial 2 on oSPARC.</td>
  </tr>   
  <tr>
    <td>
    7
    </td>
    <td> Use sparc-assemble to run the standardised workflow described in Tutorial 2 on the <a href="https://doi.org/10.52843/cassyni.6d6bvf">12 Labours Digital Twin Platform</a> (To be completed in future developments).</td>
  </tr>
</tbody>
</table>
<p align="center">
</p>
<br/>

## Reporting issues 
To report an issue or suggest a new feature, please use the [issues page](https://github.com/SPARC-FAIR-Codeathon/2024-team-3/issues). Issue templates are provided to allow users to report bugs, and documentation or feature requests. Please check existing issues before submitting a new one.

## Contributing
Fork this repository and submit a pull request to contribute. Before doing so, please read our [Code of Conduct](https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/CODE_OF_CONDUCT.md) and [Contributing Guidelines](https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/master/CONTRIBUTING.md). Pull request templates are provided to help guide developers in describing their contribution, mentioning the issues related to the pull request and describing their testing environment. 

### Project structure
* `/sparc_flow/` - Parent directory of sparc-assemble python module.
* `/sparc_flow/core/` - Core classes of sparc-assemble.
* `/resources/` - Resources that are used in tutorials (e.g. SDS datasets containing workflow and tool descriptions).
* `/tutorials/` - Parent directory of tutorials for using sparc-assemble.
* `/development_examples/` - Parent directory of examples that were created during the development of sparc-assemble.
* `/docs/images/` - Images used in sparc-assemble tutorials.

## Cite us
If you use sparc-assemble to make new discoveries or use the source code, please cite us as follows:
```
Jiali Xu, Linkun Gao, Michael Hoffman, Matthew French, Thiranja Prasad Babarenda Gamage, Chinchien Lin (2024). sparc-assemble: v1.0.0 - A Python tool to create tools and workflows for processing SPARC datasets in accordance with FAIR principles. 
Zenodo. https://doi.org/XXXX/zenodo.XXXX.
```

## FAIR practices
We have assessed the FAIRness of our sparc-assemble tool against the FAIR Principles established for research software. The details are available in the following [document](https://docs.google.com/document/d/1az_LXPivQvaofTsiMktJaWpyy2W_xKGX/edit).

## License
sparc-assemble is fully open source and distributed under the very permissive Apache License 2.0. See [LICENSE](https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/main/LICENSE) for more information.

## Team
* Mathilde Verlyck <mver587@aucklanduni.ac.nz>
* Max Dang Vu <mdan066@aucklanduni.ac.nz>,
* [Jiali Xu](https://github.com/JialiXu12) (Developer, Writer - Documentation)
* [Thiranja Prasad Babarenda Gamage](https://github.com/PrasadBabarendaGamage) (Writer - Documentation)
* [Chinchien Lin](https://github.com/LIN810116) (Lead, SysAdmin)

## Acknowledgements
- We would like to thank the organizers of the 2024 SPARC Codeathon for their guidance and support during this Codeathon.
