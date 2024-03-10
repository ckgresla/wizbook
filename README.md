# wizbook 
Writing code can be great fun, but dealing with the 0-0.1 portion of the development pipeline (the part where you have to structure your project and do the pathings) can be meh. This repository provides a tasteful and functional boilerplate for python projects, so you can focus on the fun stuff. 

Clone and get to the interesting work!


## Installation
- for development: editably install ala- `pip install -e .[dev]` (see pyproject.toml for dependencies)
- If you don't want to use the `src` dir style of python packaging, you could specify an alternate package dir with [poetry](https://python-poetry.org/docs/pyproject/) or a [setup.py script](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) 
  - for the `setup.py` method, you could create the file with something like the following contents (provided you also change up the `src` dir's structure); 
  ```python
  # setup.py
  from setuptools import setup
  setup(
      name='wizbook', # this is what folks would use to import code from the pkg
      version='0.1dev',
	  packages=['wizbook'] # name of the dir in this project repo (i.e; dir is wizbook, not src)
  ```


