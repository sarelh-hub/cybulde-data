from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass


@dataclass
class Config:
    dvc_remote_name: str = "gcs-storage"
    dvc_remote_url: str = "gs://mlops_learning_bucket/data/raw"
    dvc_raw_data_folder: str = "cybulde-data/raw"


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
