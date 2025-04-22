import pandas as pd
import joblib

def predict_attrition(df, threshold=0.5):
    model = joblib.load("outputs/model.pkl")
    X = df.drop(columns=["Attrition"], errors='ignore')
    probs = model.predict_proba(X)[:, 1]
    df['Attrition_Risk'] = probs
    high_risk_df = df[df['Attrition_Risk'] > threshold]
    high_risk_df.to_csv("outputs/high_risk_employees.csv", index=False)
    return high_risk_df
