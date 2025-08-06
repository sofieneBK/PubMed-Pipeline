"""
Utility functions for data processing and cleaning.

This module provides common utility functions for handling missing data,
parsing dates, and standardizing text across the PubMed pipeline.
"""

import re
import unicodedata

import pandas as pd


def delete_missing_data_on_column(df: pd.DataFrame, subset: str):
    """
    Remove rows with missing data in specified column.

    Args:
        df (pd.DataFrame): Input dataframe.
        subset (str): Column name to check for missing values.

    Returns:
        pd.DataFrame: Dataframe with rows containing NaN in subset column removed.
    """
    return df.dropna(subset=[subset])


def parse_date_mixed(date_str):
    """
    Parse date string with multiple format attempts.

    Tries to parse dates in the following order:
    1. %d/%m/%Y format (e.g., "01/12/2020")
    2. %d %B %Y format (e.g., "01 January 2020")
    3. Pandas to_datetime with dayfirst=True

    Args:
        date_str (str): Date string to parse.

    Returns:
        datetime or pd.NaT: Parsed datetime object or NaT if parsing fails.
    """
    from datetime import datetime
    # 1. test parsing with format %d/%m/%Y (format slash)
    try:
        return datetime.strptime(date_str, '%d/%m/%Y')
    except:
        pass
    
    # 2. test parsing with format%d %B %Y (format text month)
    try:
        return datetime.strptime(date_str, '%d %B %Y')
    except:
        pass
    
    # 3. fallback with pandas to_datetime
    try:
        return pd.to_datetime(date_str, dayfirst=True)
    except:
        return pd.NaT
    

def standardize_text(text):
    """
    Standardize text by removing accents, punctuation, and converting to lowercase.

    Performs the following operations:
    1. Replace hyphens with spaces
    2. Remove accents and diacritics
    3. Remove punctuation
    4. Convert to lowercase

    Args:
        text (str): Input text to standardize.

    Returns:
        str: Standardized text or empty string if input is null.
    """
    if pd.isnull(text):
        return ''
    # replace the '-' with spaces to not lose the word due to concatenation
    text = text.replace('-', ' ')
    # delete  accents
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    # delete ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    # to lower
    return text.lower()
