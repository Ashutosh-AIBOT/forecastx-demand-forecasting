# Product Demand Forecasting

End-to-end data analytics project on historical product demand data.

**Dataset:** [Forecasts for Product Demand – Kaggle](https://www.kaggle.com/datasets/felixzhao/productdemandforecasting)

---

## Project Structure

```
demand_forecasting/
├── data/                  # Raw CSV goes here
├── sql/                   # SQL queries (SQLite)
├── notebooks/             # Jupyter notebooks (run in Colab)
├── plots/                 # Saved charts (PNG)
├── ml/                    # Machine learning model
├── docs/                  # Project report (.docx)
└── utils/                 # Helper functions
```

---

## Setup

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl kaggle
```

---

## How to Load Data

**Option A – Kaggle API (fastest)**
```python
# In Colab:
from google.colab import files
files.upload()  # upload your kaggle.json

!mkdir -p ~/.kaggle && cp kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d felixzhao/productdemandforecasting --unzip -p data/
```

**Option B – Manual Upload in Colab**
```python
from google.colab import files
uploaded = files.upload()   # pick your CSV from laptop
```

---

## Files Overview

| File | What it does |
|------|-------------|
| `notebooks/01_eda.ipynb` | Exploratory data analysis + pandas profiling |
| `notebooks/02_visualizations.ipynb` | Static & interactive charts |
| `sql/queries.sql` | All SQL queries on the dataset |
| `ml/demand_model.py` | Random Forest demand forecast model |
| `docs/report.docx` | Written project report |

---

## Notebooks (Colab-ready)

Open each notebook in Google Colab via:
`File → Open notebook → GitHub → paste repo URL`

---

## Results

- Top warehouses and products identified by demand volume
- Seasonal demand trends visualized
- Random Forest R² ≈ 0.82 on test set

---

## Author

Built as a portfolio analytics project. Data sourced from Kaggle (Felix Zhao).
# Forecasts-for-Product-Demand-full-Analysis-
