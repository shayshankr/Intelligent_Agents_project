import os
import sys

# Ensure relative paths (data/, outputs/) resolve correctly regardless of where the script is called from
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from src.data_preprocessing import load_and_preprocess_data
from src.model_training import train_model
from src.prediction_service import predict_attrition
from src.alert_system import alert_high_risk_employees
from src.visualize import plot_risk_distribution


def run_pipeline():
    df = load_and_preprocess_data("data/HREmployeeAttrition.csv")
    train_model(df)
    high_risk_df = predict_attrition(df, threshold=0.6)
    alert_high_risk_employees(high_risk_df)
    plot_risk_distribution()


if __name__ == "__main__":
    run_pipeline()
