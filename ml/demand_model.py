"""
demand_model.py
---------------
Train a Random Forest regressor on the product demand dataset.
Run: python ml/demand_model.py --data data/demand_clean.csv
"""

import argparse
import os
import pickle
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings("ignore")


# ── CLI ───────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description="Train demand forecast model")
parser.add_argument("--data",  default="data/demand_clean.csv", help="Path to cleaned CSV")
parser.add_argument("--trees", type=int, default=100,           help="Number of RF estimators")
parser.add_argument("--depth", type=int, default=12,            help="Max tree depth")
parser.add_argument("--out",   default="ml",                    help="Output directory")
args = parser.parse_args()


# ── LOAD ──────────────────────────────────────────────────────────────────────
print(f"Loading {args.data} ...")
df = pd.read_csv(args.data, parse_dates=["Date"])
print(f"  Rows: {len(df):,}")


# ── FEATURES ─────────────────────────────────────────────────────────────────
df = df.dropna(subset=["Date"]).copy()
df["year"]        = df["Date"].dt.year
df["month"]       = df["Date"].dt.month
df["quarter"]     = df["Date"].dt.quarter
df["day_of_week"] = df["Date"].dt.dayofweek
df["day_of_year"] = df["Date"].dt.dayofyear

le = {
    "warehouse": LabelEncoder(),
    "category":  LabelEncoder(),
    "product":   LabelEncoder(),
}
df["wh_enc"]   = le["warehouse"].fit_transform(df["Warehouse"])
df["cat_enc"]  = le["category"].fit_transform(df["Product_Category"])
df["prod_enc"] = le["product"].fit_transform(df["Product_Code"])

FEATURES = ["year", "month", "quarter", "day_of_week", "day_of_year",
            "wh_enc", "cat_enc", "prod_enc"]
TARGET   = "Order_Demand"

X = df[FEATURES].values
y = df[TARGET].values


# ── SPLIT (time-based) ────────────────────────────────────────────────────────
split     = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]
print(f"  Train: {len(X_train):,}  |  Test: {len(X_test):,}")


# ── TRAIN ─────────────────────────────────────────────────────────────────────
print(f"\nTraining Random Forest (trees={args.trees}, depth={args.depth}) ...")
model = RandomForestRegressor(
    n_estimators=args.trees,
    max_depth=args.depth,
    n_jobs=-1,
    random_state=42,
)
model.fit(X_train, y_train)


# ── EVALUATE ──────────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)
mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2   = r2_score(y_test, y_pred)

print("\n── Results ──────────────────────────────")
print(f"  MAE  : {mae:,.1f}")
print(f"  RMSE : {rmse:,.1f}")
print(f"  R²   : {r2:.4f}")
print("─────────────────────────────────────────")


# ── FEATURE IMPORTANCE ────────────────────────────────────────────────────────
importance = pd.Series(model.feature_importances_, index=FEATURES).sort_values()

os.makedirs("plots", exist_ok=True)
fig, ax = plt.subplots(figsize=(7, 4))
importance.plot(kind="barh", ax=ax, color="steelblue")
ax.set_title("Feature Importance – Random Forest")
ax.set_xlabel("Importance")
plt.tight_layout()
plt.savefig("plots/feature_importance.png", dpi=150)
print("\nSaved plots/feature_importance.png")


# ── SAVE ──────────────────────────────────────────────────────────────────────
os.makedirs(args.out, exist_ok=True)

with open(os.path.join(args.out, "rf_model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(args.out, "label_encoders.pkl"), "wb") as f:
    pickle.dump(le, f)

with open(os.path.join(args.out, "features.txt"), "w") as f:
    f.write("\n".join(FEATURES))

print(f"Model saved → {args.out}/rf_model.pkl")
print(f"Encoders   → {args.out}/label_encoders.pkl")
print("\nDone.")
