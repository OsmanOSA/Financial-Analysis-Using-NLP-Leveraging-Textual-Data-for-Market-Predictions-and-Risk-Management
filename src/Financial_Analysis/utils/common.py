import os
import sys
from box.exceptions import BoxError
import yaml
from Financial_Analysis import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import joblib


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(file)
            logger.info(f"Yaml file loaded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxError as e:
        raise BoxError(f"Error loading yaml file from {path_to_yaml}") from e

@ensure_annotations
def create_dir(dir_path: list, verbose=True) -> None:
    
    for path in dir_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")

@ensure_annotations
def save_json(data: dict, path: Path, verbose=True) -> None:
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        if verbose:
            logger.info(f"Saved data to {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    
    with open(path, "r") as f:
        data = json.load(f)
        logger.info(f"Json file loaded succesfully from : {path}")
        return ConfigBox(data)


@ensure_annotations
def save_bin(data: any, path: Path, verbose=True) -> None:

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at {path}")
    

@ensure_annotations
def load_bin(path: Path) -> any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")

