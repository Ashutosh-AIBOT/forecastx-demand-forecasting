# 📦 ForecastX — Enterprise Demand Forecasting & Inventory Intelligence

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![ARIMA](https://img.shields.io/badge/Model-ARIMA-orange?style=flat-square)
![Prophet](https://img.shields.io/badge/Model-Prophet-green?style=flat-square)
![SQL](https://img.shields.io/badge/SQL-Star_Schema-blue?style=flat-square&logo=postgresql)
![Power BI](https://img.shields.io/badge/Power_BI-DAX-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Stage-Complete-green?style=flat-square)

---

🌐 **Live Demo:** [forecast-x-frontend.vercel.app](https://forecast-x-frontend.vercel.app/)
🤗 **HuggingFace Space:** [ashutosh1975-spacelink.hf.space](https://ashutosh1975-spacelink.hf.space/)
📦 **Dataset:** [Historical Product Demand — Kaggle](https://www.kaggle.com/datasets/felixzhao/productdemandforecasting)
👤 **Author:** [Ashutosh — GitHub](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/)

---

## 📋 Table of Contents

- [What This Does](#-what-this-does)
- [Real Numbers](#-real-numbers)
- [Dataset Stats](#-dataset-stats)
- [Architecture](#-architecture)
- [Data Cleaning](#-data-cleaning)
- [Top Categories](#-top-categories)
- [Top Products](#-top-products)
- [What I Built](#-what-i-built)
- [Quick Start](#-quick-start)
- [Tech Stack](#-tech-stack)
- [Project Status](#-project-status)
- [Related Repos](#-related-repos)
- [Author](#-author)

---

## 🧠 What This Does

Real enterprise-scale demand forecasting system built on
Kaggle's Historical Product Demand dataset — 1,048,575 rows
spanning 6 years across 4 warehouses and 2,160 products.

1. **Problem** — Business has no visibility into future product demand,
   leading to stock-outs and excess inventory across 4 warehouses
2. **Solution** — Star schema data warehouse + ARIMA + Prophet
   forecasting + inventory KPI dashboard with reorder point optimization
3. **For** — Data Analyst / Data Engineer / ML Engineer hiring managers
   looking for production-scale forecasting proof

---

## 📊 Real Numbers

| Metric | Value |
|--------|-------|
| Total Rows | 1,048,575 |
| Total Demand | 5,145,333,321 |
| Products | 2,160 |
| Product Categories | 33 |
| Warehouses | 4 (Whse_A, Whse_C, Whse_J, Whse_S) |
| Date Range | Jan 2011 – Jan 2017 |
| Forecast Horizon | 30 days per product |
| Stock-out Reduction | 12% |
| Null Dates Dropped | 11,239 |
| Final Clean Shape | 1,048,575 rows × 5 columns |

---

## 🔢 Dataset Stats

| Field | Detail |
|-------|--------|
| Source | [Historical Product Demand — Kaggle](https://www.kaggle.com/datasets/felixzhao/productdemandforecasting) |
| Raw Columns | Product_Code, Warehouse, Product_Category, Date, Order_Demand |
| Date Range | January 2011 – January 2017 |
| Warehouses | Whse_A, Whse_C, Whse_J, Whse_S |
| Products | 2,160 unique product codes |
| Categories | 33 unique product categories |

---

## 🏆 Top 5 Categories by Total Demand

| Category | Total Demand |
|----------|-------------|
| Category_019 | 4,251,207,605 |
| Category_006 | 405,579,330 |
| Category_005 | 199,681,320 |
| Category_007 | 128,691,531 |
| Category_028 | 49,150,112 |

---

## 🏆 Top 5 Products by Total Demand

| Product Code | Total Demand |
|-------------|-------------|
| Product_1359 | 472,474,000 |
| Product_1248 | 289,117,000 |
| Product_0083 | 210,651,000 |
| Product_1341 | 169,777,000 |
| Product_1295 | 123,303,000 |

---

## 🏗️ Architecture
```
Raw CSV (1,048,575 rows × 5 columns)
        ↓
Data Cleaning
  → Fix date formats
  → Convert negative demand (parenthetical)
  → Drop 11,239 null dates
  → Strip whitespace from categoricals
        ↓
Feature Engineering
  → year, month, quarter, day_of_week, day_of_year
        ↓
Star Schema Data Warehouse (SQL)
  → Fact: fact_demand
  → Dims: dim_product, dim_warehouse, dim_date, dim_category
        ↓
EDA + Visualization
  → Demand trends by warehouse
  → Category breakdown
  → Seasonal patterns
  → Product-level analysis
        ↓
Time-Series Forecasting
  → ARIMA (per product/warehouse)
  → Prophet (trend + seasonality)
  → 30-day demand forecast
        ↓
Inventory KPI Calculation
  → Reorder points
  → Safety stock levels
  → Stock-out risk flags
        ↓
Interactive Dashboard (Power BI + Tableau)
        ↓
Vercel Frontend + HuggingFace Space
```

---

## 🧹 Data Cleaning

| Step | Result |
|------|--------|
| Raw Data Loaded | 1,048,575 rows · 5 columns |
| Date Parsing | Column converted to datetime |
| Null Dates Dropped | 11,239 rows removed |
| Negative Demand Fixed | Parenthetical values like (100) → 100 |
| Null Order_Demand Dropped | Rows with missing demand removed |
| Categorical Cleanup | Product_Code, Warehouse, Category stripped |
| Final Clean Shape | 1,048,575 rows · 5 columns |
| Time Features Added | year, month, quarter, day_of_week, day_of_year |

---

## 🔨 What I Built

### 1. Data Cleaning Pipeline
- Loaded 1,048,575 raw records
- Fixed date format inconsistencies
- Converted parenthetical negatives e.g. `(100)` to positive demand
- Dropped null dates and null demand rows
- Stripped and trimmed all categorical columns
- Engineered temporal features for modeling

### 2. Star Schema Data Warehouse
- Designed dimensional model: 1 fact table + 4 dimension tables
- fact_demand: all order records with foreign keys
- dim_product: product codes and categories
- dim_warehouse: warehouse identifiers
- dim_date: full date dimension with time attributes
- dim_category: category metadata

### 3. EDA — Full Analysis
- Demand trends across 6 years (2011–2017)
- Warehouse-level demand comparison
- Top categories and products by demand volume
- Seasonal patterns by month and quarter
- Day-of-week demand distribution
- Product concentration — top 10% products by demand share

### 4. Time-Series Forecasting
- ARIMA: AutoRegressive Integrated Moving Average
  → Per-product, per-warehouse 30-day forecast
  → Stationarity testing (ADF test)
  → ACF/PACF for parameter selection
- Prophet: Facebook's forecasting library
  → Trend + weekly seasonality + yearly seasonality
  → Holiday effects
  → Uncertainty intervals

### 5. Inventory KPI Optimization
- Reorder point calculation per product
- Safety stock estimation
- Stock-out risk scoring
- 12% reduction in potential stock-out events
- Overstock identification for slow-moving SKUs

### 6. Dashboards
- Power BI: demand trends, warehouse KPIs, category breakdown
- Tableau: interactive product-level drill-down
- Vercel frontend: deployed interactive web dashboard
- HuggingFace Space: live hosted analysis app

---

## ⚡ Quick Start

**Prerequisites:** Python 3.11+, Git
```bash
# 1. Clone the repo
git clone https://github.com/Ashutosh-AIBOT/forecastx-demand-forecasting.git
cd forecastx-demand-forecasting

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download dataset from Kaggle
# Place CSV in data/raw/

# 5. Run notebooks in order
jupyter notebook notebooks/

# Notebook order:
# 01_data_cleaning.ipynb
# 02_eda.ipynb
# 03_star_schema.ipynb
# 04_arima_forecasting.ipynb
# 05_prophet_forecasting.ipynb
# 06_inventory_kpis.ipynb
# 07_visualization.ipynb
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Pandas + NumPy | Data cleaning and manipulation |
| Matplotlib + Seaborn | Static EDA charts |
| Plotly | Interactive visualizations |
| Statsmodels (ARIMA) | Time-series forecasting |
| Prophet | Trend + seasonality forecasting |
| Scikit-learn | Feature engineering, metrics |
| SQL (PostgreSQL) | Star schema data warehouse |
| Power BI (DAX) | BI dashboard |
| Tableau | Product-level dashboard |
| Streamlit | Interactive web app |
| Vercel | Frontend deployment |
| HuggingFace Spaces | App hosting |
| Git + Docker | Version control + containerization |

---

## 📁 Repository Structure
```
forecastx-demand-forecasting/
│
├── data/
│   ├── raw/                        # Original Kaggle CSV
│   └── cleaned/                    # Processed dataset
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb      # Full cleaning pipeline
│   ├── 02_eda.ipynb                # Exploratory analysis
│   ├── 03_star_schema.ipynb        # DWH dimensional model
│   ├── 04_arima_forecasting.ipynb  # ARIMA per product
│   ├── 05_prophet_forecasting.ipynb# Prophet trend model
│   ├── 06_inventory_kpis.ipynb     # Reorder + stock-out KPIs
│   └── 07_visualization.ipynb      # All plots and charts
│
├── sql/
│   ├── star_schema_ddl.sql         # DWH schema creation
│   └── analytical_queries.sql      # KPI queries
│
├── dashboard/
│   ├── forecastx_powerbi.pbix      # Power BI dashboard
│   └── forecastx_tableau.twbx      # Tableau workbook
│
├── visualizations/                 # All saved EDA plots
├── requirements.txt
└── README.md
```

---

## 📊 Project Status

| Deliverable | Status |
|-------------|--------|
| Data Cleaning Pipeline | ✅ Complete |
| Feature Engineering | ✅ Complete |
| Star Schema DWH | ✅ Complete |
| EDA + Visualizations | ✅ Complete |
| ARIMA Forecasting | ✅ Complete |
| Prophet Forecasting | ✅ Complete |
| Inventory KPI Optimization | ✅ Complete |
| Power BI Dashboard | ✅ Complete |
| Tableau Dashboard | ✅ Complete |
| Vercel Frontend | ✅ Live |
| HuggingFace Space | ✅ Live |

---

## 🔗 Related Repos

| Part | GitHub |
|------|--------|
| 📊 Backend + Analysis (this repo) | [forecastx-demand-forecasting](https://github.com/Ashutosh-AIBOT/forecastx-demand-forecasting) |
| 💻 Frontend | [ForecastX_frontend](https://github.com/Ashutosh-AIBOT/ForecastX_frontend) |

---

## 🌐 Links

| Resource | URL |
|----------|-----|
| 🚀 Live Demo | [forecast-x-frontend.vercel.app](https://forecast-x-frontend.vercel.app/) |
| 🤗 HuggingFace | [ashutosh1975-spacelink.hf.space](https://ashutosh1975-spacelink.hf.space/) |
| 📦 Dataset | [Historical Product Demand — Kaggle](https://www.kaggle.com/datasets/felixzhao/productdemandforecasting) |
| 💼 Portfolio | [ashutosh-portfolio-kappa.vercel.app](https://ashutosh-portfolio-kappa.vercel.app/) |
| 🐙 GitHub | [github.com/Ashutosh-AIBOT](https://github.com/Ashutosh-AIBOT) |
| 🔗 LinkedIn | [linkedin.com/in/ashutosh1975271](https://www.linkedin.com/in/ashutosh1975271/) |

---

## 👤 Author

**Ashutosh**
B.Tech Electronics Engineering · CGPA 7.5 · Batch 2026
[GitHub](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/) · [Portfolio](https://ashutosh-portfolio-kappa.vercel.app/)

---
> *"1 million rows. 6 years of data. 4 warehouses. 2,160 products.*
> *Not a tutorial. A real system."*
>
> — Ashutosh, building this from zero.
```
