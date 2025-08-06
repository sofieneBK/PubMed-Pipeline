"""
Output writer module for PubMed Pipeline.

This module provides functions to write processed data to various output formats,
primarily JSON files for drug mentions analysis results.
"""

import json
import os


def mentions_to_json(drug_mentions: dict, output_path: str):
    """
    Write drug mentions dictionary to a JSON file.

    Creates the output directory if it doesn't exist and writes the drug mentions
    data to a JSON file with proper formatting and UTF-8 encoding.

    Args:
        drug_mentions (dict): Dictionary containing drug mentions data to write.
        output_path (str): File path where the JSON file will be created.
    """
    # create the folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # file with writing rights
    with open(output_path, "w", encoding="utf-8") as f:
        # set the content of the json with the dictionnary
        json.dump(drug_mentions, f, indent=2, ensure_ascii=False)
