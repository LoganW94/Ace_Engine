import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf', 'Engine', 'Game']
base = None

if sys.platform == "win32":
	base = "Win32GUI"

setup(name = "Dungeon Miner",
	version = "0.0.1",
	description = "RPG Roguelike",
	options = {'build_exe': {'include_files': include_files}},
	executables = [Executable("main.py", base=base)])	