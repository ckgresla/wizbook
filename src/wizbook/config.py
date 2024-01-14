"""
Configuration, environment variables, et al -- ought to go in here
"""

import os
from dotenv import load_dotenv


## paths 
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)).split("/src")[0] # root dir of repo
DATA_DIR = os.path.join(PROJECT_DIR, "data")
ENVIRONMENT_FILEPATH = os.path.join(PROJECT_DIR, ".env")                  # secrets and such?


## env vars 
load_dotenv(ENVIRONMENT_FILEPATH)

print("here we go")
