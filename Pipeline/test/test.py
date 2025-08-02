import pandas as pd

from ..src.transformers.cleaner import clean


def test_remove_duplicates():
    data = {
        "title": ["Study A", "Study A", "Study B"],
        "journal": ["Journal X", "Journal X", "Journal Y"],
        "date": ["2020-01-01", "27 April 2020", "2020-01-02"]
    }
    df = pd.DataFrame(data)
    
    cleaned_df = clean(df)

    assert len(cleaned_df) == 2
    assert cleaned_df["title"].tolist() == ["Study A", "Study B"]
    print("Cleaning passed.")