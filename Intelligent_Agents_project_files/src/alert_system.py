def alert_high_risk_employees(df):
    for index, row in df.iterrows():
        print(f"[ALERT] High attrition risk detected: {row['JobRole']} - {row['Attrition_Risk']:.2f}")
