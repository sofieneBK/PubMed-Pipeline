import re

import pandas as pd


def map_drugs_to_publication_mentions(drugs_df: pd.DataFrame, publications_df: pd.DataFrame) -> dict:

    """
    For each drug in `drugs`, find publications mentioning it and
    return a dictionary mapping drug names to a list of publication details.
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