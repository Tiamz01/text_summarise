import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(levelname)s:%(message)s')

project_name = 'TextSummarizer'

list_of_project_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/logger.py",
    f"src/{project_name}/logging/exception.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "DockerFile",
    "README.md",
    "app.py",
    "main.py",
    "setup.py",
    "requirements.txt",
    "resources/trials.ipynb"

]

# creating a file directory and file

for filepath in list_of_project_files:
    filepath = Path(filepath)
    filedir, filename= os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory/folder:{filedir} for the {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, 'w') as file:
            pass
        logging.info(f"creating file:{filepath}")

    else:
        logging.info(f"filename already exists")
    