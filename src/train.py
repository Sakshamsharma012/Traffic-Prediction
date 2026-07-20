import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Saksham sharma\Desktop\Traffic prediction\data\processed\engineered_traffic.csv")
print(df.head())

df["Temp_Category"] = df["Temp_Category"].map({
    "Cold":0,
    "Moderate":1,
    "Hot":2
})

X = df.drop("traffic_volume", axis=1)
y = df["traffic_volume"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

lr = LinearRegression()

lr.fit(X_train, y_train)

predictions = lr.predict(X_test) 
print(predictions[:10])

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test, predictions)

print("MAE:", mae)

import numpy as np

rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("RMSE:", rmse)

r2 = r2_score(y_test, predictions)

print("R2 Score:", r2)

print("\nModel Performance")
print("------------------------")
print("MAE :", mae)
print("RMSE:", rmse)
print("R2  :", r2)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)
rf_predictions = rf.predict(X_test)
rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_predictions))
rf_r2 = r2_score(y_test, rf_predictions)
print("\n===== Model Comparison =====")
print(f"Linear Regression")
print(f"MAE : {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2  : {r2:.4f}")

print("\nRandom Forest")
print(f"MAE : {rf_mae:.2f}")
print(f"RMSE: {rf_rmse:.2f}")
print(f"R2  : {rf_r2:.4f}")
import joblib

joblib.dump(
    rf,
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\models\traffic_model.pkl"
)

print("✅ Model saved successfully!")