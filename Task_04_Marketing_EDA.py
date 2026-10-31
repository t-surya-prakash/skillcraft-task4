import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Task_04_Marketing_Campaign_Dataset.csv")
df["CTR"] = df["Clicks"] / df["Impressions"]
df["Conversion Rate"] = df["Conversions"] / df["Clicks"]
df["CPA"] = df["Spend"] / df["Conversions"]
df["ROAS"] = df["Revenue"] / df["Spend"]
df["ROI"] = (df["Revenue"] - df["Spend"]) / df["Spend"]

print(df.sort_values("ROAS", ascending=False))
print("\\nBest ROAS channel:", df.loc[df["ROAS"].idxmax(), "Channel"])

df.plot(x="Channel", y="ROAS", kind="bar", legend=False, title="ROAS by Channel")
plt.ylabel("ROAS (x)")
plt.tight_layout()
plt.show()
