# Ezclear lib
import os
__version__ = "0.3"
__author__ = "Unidex101@Github.com"
__license__ = "CC0"
__all__ = ["clear", "cls", "__version__", "__author__", "__license__"]

_clear_cmd = "cls" if os.name == "nt" else "clear"

def clear():
	"""Clears the terminal screen"""
	os.system(_clear_cmd)

cls = clear

if os.environ.get("MODE", "").lower() == "debug":
	print("OS:", os.name)
