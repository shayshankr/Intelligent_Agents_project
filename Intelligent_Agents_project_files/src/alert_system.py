JOB_ROLE_MAP = {
    0: "Healthcare Representative",
    1: "Human Resources",
    2: "Laboratory Technician",
    3: "Manager",
    4: "Manufacturing Director",
    5: "Research Director",
    6: "Research Scientist",
    7: "Sales Executive",
    8: "Sales Representative",
}


def alert_high_risk_employees(df):
    print(f"\n[SUMMARY] {len(df)} high-risk employees detected.\n")
    for index, row in df.iterrows():
        role_code = int(row['JobRole'])
        role_name = JOB_ROLE_MAP.get(role_code, f"Role {role_code}")
        print(f"[ALERT] Employee #{index} | Role: {role_name} | Attrition Risk: {row['Attrition_Risk']:.2f}")
