import pandas as pd

# Load dataset
df = pd.read_csv(
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\data\raw\Metro-Interstate-Traffic-Volume-Encoded.csv"
)

print("Dataset Loaded Successfully")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv(
    r"C:\Users\Saksham sharma\Desktop\Traffic prediction\data\processed\cleaned_traffic.csv",
    index=False,
)

print("\n Cleaned dataset saved successfully!")