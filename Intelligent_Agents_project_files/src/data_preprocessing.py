import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)

    # Drop EmployeeNumber and other non-informative features
    df = df.drop(columns=["EmployeeNumber", "EmployeeCount", "Over18", "StandardHours"])

    # Encode categorical columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    return df
