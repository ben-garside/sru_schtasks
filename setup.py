"""
SRU_SCHTASKS
SRU Package
-----------
python SRU_SCHTASKS
Link
`````
* Source
  https://github.com/ben-garside/
"""
from distutils.core import setup, find_packages

version = "0.1.1"

setup(
    name="sru_schtasks",
    version=version,
    author="Benjamin Garside",
    author_email="abgarside<at>gmail<dot>com",
    packages=[
        "sru",
        ],
    include_package_data=True,
    url="http://github.com/ben-garside/sru_schtasks/dist/{}/".format(version),
    description="schtasks SRU package",
    dependency_links=[
        "https://github.com/ben-garside/schtasks_shim/tarball/master#egg=schtasks_shim-0.1.1"
    ],
    install_requires=[
        "schtasks_shim>=0.1.1"
    ],
)