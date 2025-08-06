"""
Data loaders for PubMed Pipeline.
Loads clinical trials, drugs, and PubMed data from CSV/JSON files.
"""

import json

import pandas as pd

from ..config import config


def load_clinical_trials() -> pd.DataFrame:
    """Load clinical trials data from CSV file."""
    return load_csv(config.CLINICAL_TRIALS_FILE)


def load_drugs() -> pd.DataFrame:
    """Load drugs data from CSV file."""
    return load_csv(config.DRUGS_FILE)


def load_pubmed() -> pd.DataFrame:
    """Load PubMed data from CSV file."""
    return load_csv(config.PUBMED_CSV_FILE)


def load_pubmed_json() -> pd.DataFrame:
    """Load PubMed data from JSON file and convert to DataFrame."""
    return load_json(config.PUBMED_JSON_FILE)


def load_csv(path: str) -> pd.DataFrame:
    """
    Load data from CSV file.
    
    Args:
        path (str): File path to CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    return pd.read_csv(path)


def load_json(path: str) -> pd.DataFrame:
    """
    Load and normalize data from JSON file.
    
    Args:
        path (str): File path to JSON file
        
    Returns:
        pd.DataFrame: Normalized JSON data
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return pd.json_normalize(data)
