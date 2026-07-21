import joblib
import pandas as pd
model = joblib.load(
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\models\traffic_model.pkl"
)
sample = {
    "holiday":7,
    "temp":289,
    "rain_1h":0,
    "snow_1h":0,
    "Year":2024,
    "Month":8,
    "Day":12,
    "Hour":8,
    "weather_main":1,
    "weather_description":24,
    "Rush_Hour":1,
    "Rain_Flag":0,
    "Snow_Flag":0,
    "Temp_Category":1
}
sample_df = pd.DataFrame([sample])
prediction = model.predict(sample_df)
print("Predicted Traffic Volume:", int(prediction[0]))
