import os
from pathlib import Path, PurePath
import logging


logging.basicConfig(level=logging.INFO)

project_name = "mlproject.org"

list_of_files = [
    #".github/workflows/.gitkeep/master",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    print(filepath)
    filedr, filename = os.path.split(filepath)

    if filedr != "":
        os.makedirs(filedr, exist_ok=True)
        logging.info(f"Creating directory: {filedr}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath,'w') as f:
                pass # create an empty file
                logging.info(f"Creating empty file: {filepath}")

    else:
         logging.info(f"{filepath} already exists")

