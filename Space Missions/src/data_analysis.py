import pandas as pd

import pandas as pd


def analyze_launches_per_year(df):
    """
    Analyze the number of launches per year.
    """
    # Convert 'Date' column to datetime (if not already)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Now we can safely extract the year
    df['year'] = df['Date'].dt.year

    # Drop rows with invalid dates (if any)
    df = df.dropna(subset=['year'])

    launches_per_year = df.groupby('year').size()
    return launches_per_year

def analyze_cost_per_year(df):
    """
    Analyze the average cost of missions per year.
    """
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    mean_cost_per_year = df.groupby('year')['Price'].mean()
    return mean_cost_per_year