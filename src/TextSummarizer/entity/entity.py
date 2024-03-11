from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)  # Data Ingestion Entity
class DataIngestionConfig:
    """
    This class represents the configuration for data ingestion.

    Args:
        root_dir (Path): The root directory where the data is stored.
        source_URL (str): The directory where the source data is stored.
        local_data_file (Path): The path to the local data file.
        unzip_dir (Path): The directory where the data is unzipped.
    """

    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



# data validation entity
@dataclass(frozen=True)
class DataValidationConfig:
  root_dir: Path
  STATUS_FILE: str
  ALL_REQUIRED_FILE: list