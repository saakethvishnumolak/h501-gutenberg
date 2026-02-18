import pandas as pd

def clean_alias_column(df):
    
    """
    Clean the alias column by removing blanks and whitespace.
    """
    df["alias"] = df["alias"].astype(str).str.strip()
    df = df[df["alias"] != ""]
    
    return df
