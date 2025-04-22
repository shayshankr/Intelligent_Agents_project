import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_risk_distribution():
    df = pd.read_csv("outputs/high_risk_employees.csv")
    plt.figure(figsize=(10, 6))
    sns.histplot(df["Attrition_Risk"], bins=20, kde=True)
    plt.title("Attrition Risk Score Distribution")
    plt.xlabel("Predicted Risk Score")
    plt.ylabel("Employee Count")
    plt.grid(True)
    plt.savefig("outputs/attrition_risk_distribution.png")
    plt.show()
