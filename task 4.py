import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())
print(df.info())
from scipy.stats import pearsonr

# Discount మరియు Profit మధ్య correlation
corr, p = pearsonr(df["Discount"], df["Profit"])

print("\n===== Statistical Validation =====")
print("Correlation:", corr)
print("P-value:", p)

if p < 0.05:
    print("Result: Discount has a statistically significant effect on Profit.")
else:
    print("Result: Discount does not have a statistically significant effect on Profit.")