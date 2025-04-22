# HR Attrition Risk Automation

This project predicts and flags employees with a high likelihood of attrition using the IBM HR Analytics dataset.

## How It Works
- Preprocesses HR data
- Trains a Random Forest Classifier
- Predicts attrition risk scores
- Flags high-risk employees and generates alerts

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the pipeline: `python main.py`

## Output
- Trained model: `outputs/model.pkl`
- High-risk list: `outputs/high_risk_employees.csv`
