import pandas as pd

def load_data():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    return pd.read_csv(url)
