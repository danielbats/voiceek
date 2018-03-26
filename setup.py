"""Generate .exe
You will need this file to build the .exe
Please, use "pip install py2exe" in the command prompt to get the requeriments properly set.
"""

from distutils.core import setup
import py2exe

setup(windows=['voiceek.py'])
