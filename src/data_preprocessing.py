import pandas as pd

def load_data(file_path):
    """Load data from a file."""
    return pd.read_csv(file_path)

def clean_data(data):
    """Perform data cleaning, such as handling missing values."""
    data = data.dropna()
    return data

def save_processed_data(data, file_path):
    """Save the cleaned data to a new file."""
    data.to_csv(file_path, index=False)
