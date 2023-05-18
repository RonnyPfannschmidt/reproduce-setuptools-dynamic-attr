"""
this module is a hack only in place to allow for setuptools
to use the attribute for the versions
"""
from setuptools.build_meta import *

version: str

def __getattr__(name : str) -> str:
    if name == "version":
        global version
        version = "1.0"
        return version
    raise AttributeError(name)
