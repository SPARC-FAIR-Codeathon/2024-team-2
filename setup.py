import io

from setuptools import setup, find_packages
from pathlib import Path


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("package_name", "VERSION")
    >>> read("README.md")
    ...
    """

    current_dir = Path(__file__).resolve().parent
    file_path = current_dir.joinpath(*paths)
    with io.open(
            file_path,
            encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()

    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="sparc_assemble",
    version="0.1.8",
    description='A Python tool to find and automatically assemble tools and workflows to process SPARC datasets in accordance with FAIR principles.',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Thiranja Prasad Babarenda Gamage, Chinchien Lin, Jiali Xu, Mathilde Verlyck, Max Dang Vu",
    email="psam012@aucklanduni.ac.nz, clin864@aucklanduni.ac.nz",
    license="Apache-2.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['resources./*']},
    install_requires=read_requirements("requirements.txt"),
)
