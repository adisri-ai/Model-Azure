import pandas as pd
import scoring
import joblib
def predict(uploaded_file):
    # Simulate Azure's init() function
    scoring.model = joblib.load("model.pkl")  # Bypass AZUREML_MODEL_DIR

    # Read input data from Excel
    input_df = pd.read_csv(uploaded_file)

    # Create expected input format
    Inputs = {"data": input_df}
    GlobalParameters = {"method": "predict"}  # or "predict_proba"

    # Call the run() method
    results = scoring.run(Inputs, GlobalParameters)
    predictions = results["Results"]
    output_df = input_df.copy()
    output_df["Prediction"] = predictions
    return output_df

