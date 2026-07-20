import pandas as pd

df = pd.read_csv(
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\data\processed\cleaned_traffic.csv"
)

print(df.head())

def check_rush_hour(x):
    if (7 <= x <= 9) or (16 <= x <= 19):
        return 1
    else:
        return 0
    
df["Rush_Hour"] = df["Hour"].apply(
    lambda x: 1 if (7 <= x <= 9) or (16 <= x <= 19) else 0
)

def check_rush_hour(x):
    if (7 <= x <= 9) or (16 <= x <= 19):
        return 1
    else:
        return 0

lambda x: 1 if condition else 0

print(df[["Hour","Rush_Hour"]].head(20))

df["Rain_Flag"] = df["rain_1h"].apply(
    lambda x: 1 if x > 0 else 0
)

print(df[["rain_1h","Rain_Flag"]].head())

df["Snow_Flag"] = df["snow_1h"].apply(
    lambda x: 1 if x > 0 else 0
)

print(df[["snow_1h","Snow_Flag"]].head())

df["Temp_Category"] = pd.cut(
    df["temp"],
    bins=[0, 285, 295, 400],
    labels=["Cold", "Moderate", "Hot"]
)

print(df[["temp","Temp_Category"]].head())

df.to_csv(
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\data\processed\engineered_traffic.csv",
    index=False
)

df.head()