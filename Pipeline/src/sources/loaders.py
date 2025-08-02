import json

import pandas as pd

from ..config import config


def load_clinical_trials():
    return load_csv(config.CLINICAL_TRIALS_FILE)


def load_drugs():
    return load_csv(config.DRUGS_FILE)


def load_pubmed():
    return load_csv(config.PUBMED_CSV_FILE)


def load_pubmed_json():
    return load_json(config.PUBMED_JSON_FILE)


def load_csv(path: str) -> pd.DataFrame:
    """Load CSV file"""
    return pd.read_csv(path)


def load_json(path: str) -> pd.DataFrame:
    """Load JSON file"""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return pd.json_normalize(data)
