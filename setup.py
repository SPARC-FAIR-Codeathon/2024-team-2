from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="sparc_assemble",
    version="0.1.0",
    description='',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Thiranja Prasad Babarenda Gamage, Chinchien Lin, Jiali Xu, Linkun Gao, Mathilde Verlyck, Max Dang Vu",
    email="psam012@aucklanduni.ac.nz, clin864@aucklanduni.ac.nz",
    license="Apache-2.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['resources./*']},
    install_requires=[
        ""
    ]
)
