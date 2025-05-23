def is_fraud(tx: dict) -> bool:
    """
    Rule-based fraud detection function.

    A transaction is considered suspicious if:
    - It's a high-value transaction
    - The user changed their device
    - It occurred during odd hours (midnight to 4 AM)

    Parameters:
        tx (dict): A row from the DataFrame as a dictionary.

    Returns:
        bool: True if transaction is likely fraudulent, else False.
    """
    return (
        tx['high_value'] and
        tx['device_changed'] and
        tx['odd_hour']
    )


def detect_fraud(df):
    """
    Applies fraud detection rules on a DataFrame.

    Parameters:
        df (pd.DataFrame): Feature-enhanced transaction data.

    Returns:
        pd.DataFrame: Transactions flagged as fraudulent.
    """
    df['is_fraud'] = df.apply(is_fraud, axis=1)
    return df[df['is_fraud'] == True]
