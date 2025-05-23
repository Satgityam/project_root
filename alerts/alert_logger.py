import pandas as pd
import os

def log_alerts(frauds_df: pd.DataFrame, path: str = "alerts/alerts.csv"):
    """
    Saves detected frauds to a CSV file.

    Parameters:
        frauds_df (pd.DataFrame): DataFrame with flagged transactions.
        path (str): Path to save the alert file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    frauds_df.to_csv(path, index=False)
    print(f"🔔 {len(frauds_df)} fraud transactions logged to {path}")
