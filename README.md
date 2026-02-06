# Retail Retention ML Project

ML-based system for personalized customer retention offers for the «В один клик» e-commerce store

## Goal

- **Classification model** — predict decline in customer purchase activity  
- **Customer segmentation** — by model outputs and profitability  
- **Personalized offers** — per segment for retention and profit

## Repository structure

```
.
├── notebook.ipynb      # Full pipeline: EDA, preprocessing, modeling, SHAP, segmentation
├── market_file.csv     # Main customer data (target: покупательская активность)
├── market_money.csv    # Revenue by period per customer
├── market_time.csv     # Time on site by period
├── money.csv           # Customer profitability (last 3 months)
├── requirements.txt   # Python dependencies
└── README.md
```

## Requirements

- Python 3.10+
- Dependencies: see `requirements.txt`

## Setup and run

```bash
# Clone and enter project
git clone https://github.com/danlikendy/retail-retention-ml-project.git
cd retail-retention-ml-project

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run notebook (Jupyter)
jupyter notebook notebook.ipynb
```

Data files (`market_file.csv`, `market_money.csv`, `market_time.csv`, `money.csv`) must be in the project root or in `/datasets/` (notebook checks both)

## Methods

| Area            | Tools / approach                                      |
|-----------------|--------------------------------------------------------|
| Data            | pandas, numpy                                         |
| Visualization   | matplotlib, seaborn                                   |
| Models          | KNeighborsClassifier, DecisionTreeClassifier, LogisticRegression, SVC (sklearn) |
| Preprocessing   | ColumnTransformer, Pipeline, StandardScaler, OneHotEncoder |
| Explainability  | SHAP                                                  |
| Metrics         | F1-score, ROC-AUC, accuracy, precision, recall         |

## Success criteria

- Best model: **F1-score ≥ 0.7**, **ROC-AUC ≥ 0.8**
- Segments with clear, actionable retention offers

## License

MIT
