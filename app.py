import streamlit as st
import pandas as pd
import test_run
import joblib
st.set_page_config(page_title="Stock Prediction App", layout="centered")
st.title("📈 Stock Prediction App")

uploaded_file = st.file_uploader("Upload CSV file with stock data", type=["csv"])

if uploaded_file is not None:
    try:
        # Read input CSV into DataFrame
        output_df = test_run.predict(uploaded_file)
        # Prepare Inputs in the format expected by scoring.py

        # Show results
        st.subheader("✅ Predictions with Stock Names")
        # Prepare CSV for download
        csv = output_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Results as CSV",
            data=csv,
            file_name="stock_predictions.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error: {e}")
