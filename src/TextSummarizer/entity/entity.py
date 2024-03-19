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


# data transformation entity
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

# model trainer entity
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int 
    weight_decay: float 
    logging_steps:int
    evaluation_strategy: str
    eval_steps: int 
    save_steps: float
    gradient_accumulation_steps: int

# model evaluation entity
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path
