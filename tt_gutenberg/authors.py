import pandas as pd
from .data import load_data
from .utils import clean_alias_column

def list_authors(by_languages=True, alias=True):
    """
    Return author aliases ordered by translation count.
    """

    # Load dataset
    df = load_data()

    # Update column name to match the CSV
    df = df.rename(columns={"author": "alias"})

    # Clean alias values
    df = clean_alias_column(df)

    # Count translations per alias
    counts = df.groupby("alias").size().sort_values(ascending=False)

    return counts.index.tolist()


