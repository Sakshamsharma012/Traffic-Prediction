import streamlit as st
import pandas as pd
import joblib
model = joblib.load(
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\models\traffic_model.pkl"
)
st.title("Traffic Volume Prediction")
temp = st.number_input("Temperature")
hour = st.slider("Hour",0,23)
rain = st.number_input("Rain")
snow = st.number_input("Snow")
holiday = st.number_input("Holiday")
weather_main = st.number_input("Weather Main")
weather_description = st.number_input("Weather Description")
rush_hour = 1 if (7<=hour<=9) or (16<=hour<=19) else 0
rain_flag = 1 if rain>0 else 0
snow_flag = 1 if snow>0 else 0
if temp<285:
    temp_category=0

elif temp<295:
    temp_category=1

else:
    temp_category=2

if st.button("Predict"):

    input_data = pd.DataFrame({
        "holiday": [holiday],
        "temp": [temp],
        "rain_1h": [rain],
        "snow_1h": [snow],
        "Year": [2024],
        "Month": [8],
        "Day": [15],
        "Hour": [hour],
        "weather_main": [weather_main],
        "weather_description": [weather_description],
        "Rush_Hour": [rush_hour],
        "Rain_Flag": [rain_flag],
        "Snow_Flag": [snow_flag],
        "Temp_Category": [temp_category]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Traffic Volume: {int(prediction[0])}")