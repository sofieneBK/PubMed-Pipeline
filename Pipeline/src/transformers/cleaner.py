"""
Data cleaning and transformation module for PubMed Pipeline.

This module provides functions to clean and process clinical trials, PubMed,
and drugs data for analysis.
"""

import numpy as np

from ..utils.utils import *


def process_clinical_trials_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process clinical trials dataframe by renaming columns and merging rows.

    Args:
        df (pd.DataFrame): Raw clinical trials dataframe.

    Returns:
        pd.DataFrame: Processed clinical trials dataframe with 'source' column.
    """

    # rename column : 
    df = df.rename(columns={"scientific_title": "title"})

    # merge the rows that has the value "title" or "date" with those with NAN 
    original_columns = df.columns  # Save the original order
    grouped = df.groupby(["title"], dropna=False)
    df = grouped.agg(lambda x: x.dropna().iloc[0] if x.dropna().any() else np.nan).reset_index()
    df = df.reset_index()[original_columns]

    df['source'] = "clinical_trials"
    
    return df



def process_pubmed_dataframe(pubcsv: pd.DataFrame, pubjson: pd.DataFrame) -> pd.DataFrame:
    """
    Process PubMed CSV and JSON dataframes into a single dataframe.

    Args:
        pubcsv (pd.DataFrame): PubMed data from CSV file.
        pubjson (pd.DataFrame): PubMed data from JSON file.

    Returns:
        pd.DataFrame: Combined PubMed dataframe with 'source' column.
    """
    df = pd.concat([pubcsv, pubjson], ignore_index=True)
    
    #  column source to know which source it came from
    df['source'] = "pubmed"

    return df


def process_drugs(drug: pd.DataFrame) -> pd.DataFrame:
    """
    Process drugs data by standardizing drug names.

    Args:
        drug (pd.DataFrame): Raw drugs dataframe.

    Returns:
        pd.DataFrame: Processed drugs dataframe with standardized drug names.
    """
    drug['drug'] = drug['drug'].apply(standardize_text)
    return drug



def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply global cleaning operations to any dataframe.

    Performs the following operations:
    - Replace empty strings with NaN values
    - Remove rows with missing titles
    - Parse and standardize dates
    - Standardize text in title and journal columns

    Args:
        df (pd.DataFrame): Input dataframe to clean.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    
    # manage spaces and replace them with NaN values
    for column in df.columns:
        df[column] = df[column].replace(r'^\s*$', np.nan, regex=True)

    # delete NaN titles
    df = delete_missing_data_on_column(df, "title")

    # date processing
    df['date'] = df['date'].apply(parse_date_mixed)
    
    # standarization (lower, accents, spaces, commas, ...)
    df['title'] = df['title'].apply(standardize_text)
    df['journal'] = df['journal'].apply(standardize_text)

    return df