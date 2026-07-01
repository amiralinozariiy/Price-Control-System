import pandas as pd

data = {
    "Product": ["Burger", "Pizza", "Sandwich", "Salad"],
    "Previous Price": [120000, 180000, 90000, 70000],
    "Current Price": [130000, 175000, 95000, 75000]
}

df = pd.DataFrame(data)

df["Difference"] = df["Current Price"] - df["Previous Price"]
df["Change %"] = ((df["Difference"] / df["Previous Price"]) * 100).round(2)

print(df)
