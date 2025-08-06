"""
Drug mentions mapping module for PubMed Pipeline.

This module provides functionality to map drugs to publications that mention them,
creating a comprehensive dictionary of drug-publication relationships.
"""

import re

import pandas as pd


def map_drugs_to_publication_mentions(drugs_df: pd.DataFrame, publications_df: pd.DataFrame) -> dict:
    """
    Map each drug to publications that mention it in their titles.

    Searches for exact word matches of drug names in publication titles using
    regex patterns. Returns a dictionary where each drug name maps to a list
    of publication details that mention that drug.

    Args:
        drugs_df (pd.DataFrame): DataFrame containing drug information with 'drug' column.
        publications_df (pd.DataFrame): DataFrame containing publication data with columns:
            - 'title': Publication title to search in
            - 'journal': Publication journal name
            - 'date': Publication date
            - 'source': Publication source

    Returns:
        dict: Dictionary mapping drug names (str) to lists of publication dictionaries.
              Each publication dictionary contains:
              - 'title': Publication title
              - 'journal': Journal name
              - 'date': Publication date
              - 'source': Publication source

    Note:
        Uses whole-word matching to avoid partial matches (e.g., 'aspirin' won't 
        match 'aspirinate'). Drug names with special regex characters are 
        automatically escaped.
    """

    drug_mentions_map = {}

    for drug_name in drugs_df['drug']:
        # Ensure special characters in the drug name don't break the regex
        escaped_name = re.escape(drug_name)

        # Match drug name as a whole word
        search_pattern = rf"\b{escaped_name}\b"

        # Select publications where title contains the drug name
        matched_publications = publications_df[
            publications_df['title'].str.contains(search_pattern, na=False, regex=True)
        ]

        # Convert matched publications to a list of dicts
        publication_details = [
            {
                'title': pub['title'],
                'journal': pub['journal'],
                'date': pub['date'],
                'source': pub['source']
            }
            for _, pub in matched_publications.iterrows()
        ]

        # Store in result mapping
        drug_mentions_map[drug_name] = publication_details

    return drug_mentions_map