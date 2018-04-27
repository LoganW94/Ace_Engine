import sys
from cx_Freeze import setup, Executable
from Engine.ace_engine import AceEngine

include_files = ['autorun.inf', 'Engine']
base = None

if sys.platform == "win32":
	base = "Win32GUI"

setup(name = "Dungeon Miner",
	version = "0.0.1",
	description = "RPG Roguelike",
	options = {'build_exe': {'include_files': include_files}},
	executables = [Executable("main.py", base=base)])	