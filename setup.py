import sys
from cx_Freeze import setup, Executable


setup(
    name = "Hour Calculator",
    version = "0.1",
    description = "Calculate Hours",
    executables = [Executable("HourConverter.py")])
