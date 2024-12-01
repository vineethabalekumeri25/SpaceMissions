import pandas as pd


def load_data(file_path):
    """
    Load the dataset and preprocess it.
    """
    df = pd.read_csv(file_path)

    # Print column names for debugging
    print(f"Loaded Columns: {df.columns}")

    # Ensure 'launch_date' is in datetime format, if present
    if 'Date' in df.columns:
        df['launch_date'] = pd.to_datetime(df['Date'], errors='coerce')
    else:
        print("Warning: 'launch_date' column not found.")

    # Ensure 'mission_cost' column is numeric, if present (updated from 'cost' to 'mission_cost')
    if 'Price' in df.columns:
        df['mission_cost'] = pd.to_numeric(df['Price'], errors='coerce')  # Use 'mission_cost' instead of 'cost'
    else:
        print("Warning: 'mission_cost' column not found.")

    return df