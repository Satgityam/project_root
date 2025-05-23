from engine.feature_extractor import extract_features
from engine.fraud_detector import detect_fraud
from alerts.alert_logger import log_alerts

if __name__ == "__main__":
    # Load and process transactions
    df = extract_features("data/transactions.csv")

    # Detect fraudulent transactions
    frauds = detect_fraud(df)

    # Log detected fraud alerts
    log_alerts(frauds)
