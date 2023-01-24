from platform import system
import os
from setuptools import setup
#This program installs missing dependancies
setup(name="cursesplus",version="0.2.0")
if system == "Windows":
    os.system("py -m pip install windows-curses")