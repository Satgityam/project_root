import pandas as pd

def extract_features(csv_path: str) -> pd.DataFrame:
    """
    Reads the transactions CSV and adds derived features.

    Parameters:
        csv_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame with additional features.
    """
    df = pd.read_csv(csv_path)

    # Derived features
    df['high_value'] = df['amount'] > 10000  # True if transaction amount is high
    df['odd_hour'] = df['hour'].isin([0, 1, 2, 3])  # True if transaction at odd hour
    df['device_changed'] = df['device_change'] == 1  # Convert int to bool for clarity

    return df

# Test (you can remove this part in production)
if __name__ == "__main__":
    df = extract_features("data/transactions.csv")
    print(df.head())
