import streamlit as st
import pandas as pd
import joblib
from datetime import date

model = joblib.load(
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\models\traffic_model.pkl"
)
st.set_page_config(
    page_title="Traffic Volume Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Traffic Volume Prediction")

st.write(
    "Predict hourly traffic volume using Machine Learning."
)
temp_c = st.number_input(
    "🌡 Temperature (°C)",
    min_value=-30.0,
    max_value=50.0,
    value=25.0
)

temp = temp_c + 273.15
selected_date = st.date_input(
    "📅 Select Date",
    value=date.today()
)

year = selected_date.year
month = selected_date.month
day = selected_date.day
hour = st.slider(
    "⏰ Hour of the Day",
    0,
    23,
    8
)
rain = st.number_input(
    "🌧 Rainfall (mm)",
    min_value=0.0,
    value=0.0
)
snow = st.number_input(
    "❄ Snowfall (mm)",
    min_value=0.0,
    value=0.0
)
holiday_option = st.radio(

    "🎉 Is it a Holiday?",

    ["No","Yes"]

)

if holiday_option=="No":
    holiday=7

else:
    holiday=0

weather = st.selectbox(

    "🌦 Weather",

    [

        "Clear",

        "Clouds",

        "Rain",

        "Mist",

        "Fog",

        "Snow"

    ]

)
weather_encoding = {

    "Clear":0,

    "Clouds":1,

    "Rain":2,

    "Mist":3,

    "Fog":4,

    "Snow":5

}
weather_main = weather_encoding[weather]

weather_description = weather_encoding[weather]
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

    "holiday":[holiday],

    "temp":[temp],

    "rain_1h":[rain],

    "snow_1h":[snow],

    "Year":[year],

    "Month":[month],

    "Day":[day],

    "Hour":[hour],

    "weather_main":[weather_main],

    "weather_description":[weather_description],

    "Rush_Hour":[rush_hour],

    "Rain_Flag":[rain_flag],

    "Snow_Flag":[snow_flag],

    "Temp_Category":[temp_category]

    })
   
    prediction = model.predict(input_data)

    traffic = int(prediction[0])

    if traffic < 2000:
        level = "🟢 Low Traffic"

    elif traffic < 4500:
        level = "🟠 Moderate Traffic"

    else:
        level = "🔴 Heavy Traffic"

    st.success(f"Predicted Traffic Volume: {traffic} vehicles/hour")

    st.info(level)