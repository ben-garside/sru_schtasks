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
from distutils.core import setup

version = "0.1.0"

setup(
    name="sru_schtasks",
    version=version,
    author="Benjamin Garside",
    author_email="abgarside<at>gmail<dot>com",
    packages=[
        "sru_schtasks"
        ],
    include_package_data=True,
    url="http://github.com/ben-garside/sru_schtasks/dist/{}/".format(version),

    # license="LICENSE.txt",
    description="schtasks SRU package",
    long_description=open("README.md").read(),
    # Dependent packages (distributions)
    install_requires=[
        "voluptuous",
        "aiohttp",
        "git+https://github.com/ben-garside/schtasks_shim"
    ],
)