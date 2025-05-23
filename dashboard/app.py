import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from engine.feature_extractor import extract_features
from engine.fraud_detector import detect_fraud

st.set_page_config(page_title="UPI Fraud Detector", layout="wide")
st.title("📊 Real-Time UPI Fraud Detection Dashboard")

# Load data
csv_path = "data/transactions.csv"
try:
    df = extract_features(csv_path)
    frauds = detect_fraud(df)

    st.subheader("🚨 Detected Fraudulent Transactions")
    st.dataframe(frauds, use_container_width=True)

    st.subheader("📈 Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transactions", len(df))
    col2.metric("Flagged Frauds", len(frauds))
    col3.metric("Fraud Rate", f"{(len(frauds) / len(df) * 100):.2f}%")

    st.subheader("📌 Filter Fraud Transactions")
    amount_threshold = st.slider("Minimum Amount", 0, 20000, 5000)
    filtered = frauds[frauds['amount'] >= amount_threshold]
    st.dataframe(filtered)

    # Hourly fraud distribution heatmap
    st.subheader("🕒 Fraud Transactions by Hour of Day")
    frauds_by_hour = frauds['hour'].value_counts().sort_index()
    
    fig, ax = plt.subplots(figsize=(10,4))
    sns.barplot(x=frauds_by_hour.index, y=frauds_by_hour.values, palette="Reds", ax=ax)
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Number of Fraud Transactions")
    ax.set_title("Fraud Transactions Distribution by Hour")
    st.pyplot(fig)

    # Top risky users
    st.subheader("👤 Top Users with Most Fraud Transactions")
    top_users = frauds['user_id'].value_counts().head(10)
    fig2, ax2 = plt.subplots(figsize=(10,4))
    sns.barplot(x=top_users.index, y=top_users.values, palette="Blues", ax=ax2)
    ax2.set_xlabel("User ID")
    ax2.set_ylabel("Fraud Transaction Count")
    ax2.set_title("Top 10 Risky Users")
    st.pyplot(fig2)

except FileNotFoundError:
    st.error("🚫 transactions.csv not found. Please run the simulator first.")
