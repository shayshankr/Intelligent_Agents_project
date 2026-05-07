# HR Attrition Risk Automation — Intelligent Agents Project

An intelligent agent pipeline that predicts and flags employees with a high likelihood of leaving, using the IBM HR Analytics dataset and a Random Forest classifier.

---

## How It Works

1. **Data Preprocessing** — Loads the HR dataset, drops non-informative columns, and label-encodes categorical features
2. **Model Training** — Trains a Random Forest classifier (class-weighted for imbalance) and saves the model to `outputs/model.pkl`
3. **Prediction** — Scores every employee with an attrition risk probability; employees above the threshold (default: 0.6) are flagged
4. **Alert System** — Prints a human-readable alert for each high-risk employee with their role and risk score
5. **Visualisation** — Saves a risk score distribution histogram to `outputs/attrition_risk_distribution.png`

## Project Structure

```
Intelligent_Agents_project_files/
├── main.py                        # Pipeline entry point
├── requirements.txt               # Python dependencies
├── data/
│   └── HREmployeeAttrition.csv    # IBM HR Analytics dataset (1,470 employees)
├── outputs/
│   ├── model.pkl                  # Trained Random Forest model
│   ├── high_risk_employees.csv    # Flagged high-risk employees
│   └── attrition_risk_distribution.png
├── src/
│   ├── data_preprocessing.py      # Load and encode dataset
│   ├── model_training.py          # Train and save model
│   ├── prediction_service.py      # Score employees and filter high-risk
│   ├── alert_system.py            # Print alerts for high-risk employees
│   └── visualize.py               # Plot risk score distribution
└── BPMN.drawio.png                # BPMN process diagram
```

## How to Run

```bash
git clone https://github.com/shayshankr/Intelligent_Agents_project.git
cd Intelligent_Agents_project/Intelligent_Agents_project_files
pip install -r requirements.txt
python main.py
```

The pipeline can also be run from the repo root:

```bash
python Intelligent_Agents_project_files/main.py
```

## Output Example

```
[SUMMARY] 197 high-risk employees detected.

[ALERT] Employee #0   | Role: Sales Executive        | Attrition Risk: 0.74
[ALERT] Employee #2   | Role: Laboratory Technician  | Attrition Risk: 0.75
[ALERT] Employee #14  | Role: Laboratory Technician  | Attrition Risk: 0.84
...
```

## Model Performance

| Metric | Score |
|---|---|
| Accuracy | 87% |
| Precision (Attrition) | 67% |
| Recall (Attrition) | 10% |
| ROC AUC | ~0.85 |

## Requirements

- Python 3.10+
- pandas, scikit-learn, matplotlib, seaborn, joblib

## Author

- **Name:** Shayshank Rathore
- **Student ID:** x23348186
- **Email:** x23348186@student.ncirl.ie
