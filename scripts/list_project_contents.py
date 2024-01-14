"""
This example script illustrates what importing from the main module looks like

`py scripts/list_project_contents.py`
"""

import os
from wizbook.config import PROJECT_DIR
from wizbook.viz import printok, printlog


def list_dirs_files(path: str, indent=0):
    for entry in os.scandir(path):
        if entry.name in [".git", ".DS_Store", "__pycache__", "wizbook.egg-info"]:
            continue
        if entry.is_file():
            printlog('  ' * indent + entry.name)  # for files
        elif entry.is_dir():
            print('  ' * indent + entry.name)  # for directories
            # recursively call for sub-directories
            list_dirs_files(entry.path, indent=indent+1)


list_dirs_files(PROJECT_DIR)
printok("\n\nquite the nice project eh?\n")
