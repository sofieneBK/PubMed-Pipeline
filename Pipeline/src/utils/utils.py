import re
import unicodedata

import pandas as pd


def delete_missing_data_on_column(df: pd.DataFrame, subset: str):
    return df.dropna(subset=[subset])


def parse_date_mixed(date_str):
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



    