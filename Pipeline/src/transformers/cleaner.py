import numpy as np

from ..utils.utils import *


############## process clinical trials data
def process_clinical_trials_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    # rename column : 
    df = df.rename(columns={"scientific_title": "title"})

    # merge the rows that has the value "title" or "date" with those with NAN 
    original_columns = df.columns  # Save the original order
    grouped = df.groupby(["title"], dropna=False)
    df = grouped.agg(lambda x: x.dropna().iloc[0] if x.dropna().any() else np.nan).reset_index()
    df = df.reset_index()[original_columns]

    df['source'] = "clinical_trials"
    
    return df


############## process pubmed data
def process_pubmed_dataframe(pubcsv: pd.DataFrame, pubjson: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([pubcsv, pubjson], ignore_index=True)
    
    #  column source to know which source it came from
    df['source'] = "pubmed"

    return df

############## process drugs data
def process_drugs(drug: pd.DataFrame) -> pd.DataFrame:
    drug['drug'] = drug['drug'].apply(standardize_text)
    return drug


# ########### Global cleaning
def clean(df: pd.DataFrame)-> pd.DataFrame:
    
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